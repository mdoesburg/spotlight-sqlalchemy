from typing import Any, List

from spotlight_sqlalchemy import errors
from spotlight.rules import Rule


class UniqueRule(Rule):
    """Unique database record"""

    name = "unique"

    def __init__(self, session):
        super().__init__()
        self._session = session

    def passes(self, field: str, value: Any, parameters: List[str], validator) -> bool:
        self.message_fields = dict(field=field)
        table, column, *extra = parameters

        ignore_col = extra[0] if len(extra) > 0 else None
        ignore_val = extra[1] if len(extra) > 1 else None
        where_col = extra[2] if len(extra) > 2 else None
        where_val = extra[3] if len(extra) > 3 else None

        exists = self._unique_check(
            value, table, column, ignore_col, ignore_val, where_col, where_val
        )

        return not exists

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
        query = "SELECT * FROM {table} WHERE {column} = :value1".format(
            table=table, column=column
        )
        params = {"value1": value}

        # If ignore values are set
        if ignore_col and ignore_val and ignore_col != "null" and ignore_val != "null":
            query += " AND {} != :ignore_val".format(ignore_col)
            params["ignore_val"] = ignore_val

        # If where values are set
        if where_col and where_val:
            query += " AND {where_col} = :where_val".format(where_col=where_col)
            params["where_val"] = where_val

        result = self._session.execute(query, params).first()

        return result

    @property
    def message(self) -> str:
        return errors.UNIQUE_ERROR


class ExistsRule(Rule):
    """Exists in database"""

    name = "exists"

    def __init__(self, session):
        super().__init__()
        self._session = session
        self.error = None

    def passes(self, field: str, value: Any, parameters: List[str], validator) -> bool:
        table, column, *extra = parameters

        # Check if extra where is set
        if extra:
            where_col = extra[0]
            where_val = extra[1]
            self.message_fields = dict(field=field, other=where_col)
            self.error = errors.EXISTS_WHERE_ERROR

            query = (
                "SELECT * FROM {table} WHERE {column} = :value1 "
                "AND {where_col} = :value2".format(
                    table=table, column=column, where_col=where_col
                )
            )
            params = {"value1": value, "value2": where_val}
            exists = self._session.execute(query, params).first()
        else:
            self.message_fields = dict(field=field)
            self.error = errors.EXISTS_ERROR

            query = "SELECT * FROM {table} WHERE {column} = :value1".format(
                table=table, column=column
            )
            params = {"value1": value}
            exists = self._session.execute(query, params).first()

        return exists

    @property
    def message(self) -> str:
        return self.error
