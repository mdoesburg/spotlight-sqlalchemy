import unittest

from spotlight_sqlalchemy.plugin import SqlAlchemyPlugin
from spotlight_sqlalchemy.tests.database import Base, session, User
from spotlight.validator import Validator


class SqlAlchemyPluginTest(unittest.TestCase):

    _session = None

    @classmethod
    def setUpClass(cls):
        cls._setUpDatabase()
        cls.validator = Validator([SqlAlchemyPlugin(cls._session)])

    @classmethod
    def _setUpDatabase(cls):
        cls._session = session()
        cls._load_fixtures()

    @classmethod
    def _load_fixtures(cls):
        _engine = cls._session.get_bind()

        Base.metadata.drop_all(_engine)
        Base.metadata.create_all(_engine)

        users = [
            User(
                first_name="John",
                last_name="Doe",
                email="john.doe@example.com",
                phone="555-539-4123",
                password="this.is.a.test.password",
                site_id=1,
            ),
            User(
                first_name="Jane",
                last_name="Doe",
                email="jane.doe@example.com",
                phone="555-540-5244",
                password="this.is.a.test.password",
                site_id=2,
            ),
        ]
        cls._session.add_all(users)
        cls._session.commit()

    @classmethod
    def tearDownClass(cls):
        cls._session.close()
