from spotlight import errors
from spotlight.rules import BaseRule, DependentRule


class SessionRule(BaseRule):
    def __init__(self, session):
        super().__init__()
        self._session = session

    def message(self) -> str:
        pass


class UniqueRule(DependentRule, SessionRule):
    """Unique database record"""

    name = "unique"

    def passes(self, field, value, rule_values, input_) -> bool:
        self.message_fields = dict(field=field)
        table, column, *extra = rule_values[0].split(",")

        ignore_col = extra[0] if len(extra) > 0 else None
        ignore_val = extra[1] if len(extra) > 1 else None
        where_col = extra[2] if len(extra) > 2 else None
        where_val = extra[3] if len(extra) > 3 else None

        exists = self._unique_check(
            value, table, column, ignore_col, ignore_val, where_col, where_val
        )

        return not exists

    def message(self) -> str:
        return errors.UNIQUE_ERROR

    def _unique_check(
        self,
        value,
        table,
        column,
        ignore_col=None,
        ignore_val=None,
        where_col=None,
        where_val=None,
    ):
        # Create query
        query = "SELECT * FROM {} WHERE {} = :value1".format(table, column)
        params = {"value1": value}

        # If ignore values are set
        if ignore_col and ignore_val and ignore_col != "null" and ignore_val != "null":
            query += " AND {} != :ignore_val".format(ignore_col)
            params["ignore_val"] = ignore_val

        # If where values are set
        if where_col and where_val:
            query += " AND {} = :where_val".format(where_col)
            params["where_val"] = where_val

        result = self._session.execute(query, params).first()

        return result


class ExistsRule(DependentRule, SessionRule):
    """Exists in database"""

    name = "exists"

    def __init__(self, session):
        super().__init__(session)
        self.error = None

    def passes(self, field, value, rule_values, input_) -> bool:
        table, column, *extra = rule_values[0].split(",")

        # Check if extra where is set
        if extra:
            where_col = extra[0]
            where_val = extra[1]
            self.message_fields = dict(field=field, other=where_col)
            self.error = errors.EXISTS_WHERE_ERROR

            query = "SELECT * FROM {} WHERE {} = :value1 " "AND {} = :value2".format(
                table, column, where_col
            )
            params = {"value1": value, "value2": where_val}
            exists = self._session.execute(query, params).first()
        else:
            self.message_fields = dict(field=field)
            self.error = errors.EXISTS_ERROR

            query = "SELECT * FROM {} WHERE {} = :value1".format(table, column)
            params = {"value1": value}
            exists = self._session.execute(query, params).first()

        return exists

    def message(self) -> str:
        return self.error
