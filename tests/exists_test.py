from src.spotlight_sqlalchemy import errors as err
from .plugin_test import SqlAlchemyPluginTest


class ExistsTest(SqlAlchemyPluginTest):
    def test_exists_rule_with_existing_id_expect_no_error(self):
        field = "id"
        rules = {"id": "exists:user,id"}
        data = {"id": 1}
        expected = None

        errors = self.validator.validate(data, rules)
        errs = errors.get(field)

        self.assertEqual(errs, expected)

    def test_exists_rule_with_non_existing_id_expect_error(self):
        field = "id"
        rules = {"id": "exists:user,id"}
        data = {"id": 3}
        expected = err.EXISTS_ERROR.format(field=field)

        errors = self.validator.validate(data, rules)
        errs = errors.get(field)

        self.assertEqual(errs[0], expected)

    def test_exists_rule_with_non_existing_email_for_id_expect_error(self):
        field = "email"
        other = "id"
        rules = {"email": "exists:user,email,id,1"}
        data = {"email": "john.doe2@example.com"}
        expected = err.EXISTS_WHERE_ERROR.format(field=field, other=other)

        errors = self.validator.validate(data, rules)
        errs = errors.get(field)

        self.assertEqual(errs[0], expected)

    def test_exists_rule_with_existing_email_for_id_expect_no_error(self):
        field = "email"
        rules = {"email": "exists:user,email,id,1"}
        data = {"email": "john.doe@example.com"}
        expected = None

        errors = self.validator.validate(data, rules)
        errs = errors.get(field)

        self.assertEqual(errs, expected)
