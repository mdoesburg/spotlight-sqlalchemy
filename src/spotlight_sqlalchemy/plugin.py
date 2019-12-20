from spotlight.validator import Validator

from . import rules


class SQLAlchemyPlugin(Validator.Plugin):
    def __init__(self, session):
        self._session = session

    def rules(self):
        return [rules.UniqueRule(self._session), rules.ExistsRule(self._session)]
