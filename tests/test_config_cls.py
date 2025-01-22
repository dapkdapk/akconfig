import unittest

from ak.config import \
    AKConfig  # Replace 'your_module' with the actual module name


class TestAKConfig(unittest.TestCase):

    def setUp(self):
        # Setting up a basic environment for tests
        self.global_vars = {
            "string_var": "test_string",
            "int_var": 10,
            "float_var": 10.5,
            "bool_var": "True",
            "list_var": "item1,item2",
            "dict_var": '{"key": "value"}',
        }
        self.config_params = (
            ("string_var", "updated_string"),
            ("int_var", "20"),
            ("float_var", "15.5"),
            ("bool_var", "False"),
            ("list_var", "item3,item4"),
            ("dict_var", '{"new_key": "new_value"}'),
        )
        self.mask_keys = ["string_var", "dict_var"]
        self.ak_config = AKConfig(self.global_vars, self.config_params, self.mask_keys)

    def test_initialization(self):
        self.assertEqual(self.ak_config.string_var, "updated_string")
        self.assertEqual(self.ak_config.int_var, 20)
        self.assertEqual(self.ak_config.float_var, 15.5)
        self.assertEqual(self.ak_config.list_var, "item3,item4")
        self.assertEqual(self.ak_config.dict_var, '{"new_key": "new_value"}')

    def test_set_valid_attribute(self):
        self.ak_config.set("string_var", "new_value")
        self.assertEqual(self.ak_config.string_var, "new_value")

    def test_set_invalid_attribute(self):
        self.ak_config.set("non_existing_var", "value")
        self.assertEqual(
            self.ak_config.string_var, "updated_string"
        )  # Should remain unchanged

    def test_set_none_value(self):
        self.ak_config.set("string_var", None)
        self.assertEqual(
            self.ak_config.string_var, "updated_string"
        )  # Should remain unchanged

    def test_params_update(self):
        new_params = (
            ("string_var", "another_string"),
            ("int_var", "30"),
        )
        self.ak_config.arguments(new_params)
        self.assertEqual(self.ak_config.string_var, "another_string")
        self.assertEqual(self.ak_config.int_var, 30)

    def test_get_attributes(self):
        attributes = self.ak_config.get_attributes()
        expected_attributes = [
            "string_var",
            "int_var",
            "float_var",
            "bool_var",
            "list_var",
            "dict_var",
        ]
        self.assertTrue(all(attr in attributes for attr in expected_attributes))

    def test_get_config(self):
        config = self.ak_config.get_config(add_type=True)
        self.assertIn("string_var (\x1b[38;5;12mstr\x1b[0m)", config)
        self.assertIn("int_var (\x1b[38;5;11mint\x1b[0m)", config)
        self.assertIn("float_var (\x1b[38;5;37mfloat\x1b[0m)", config)

    def test_casting(self):
        self.assertEqual(AKConfig.Cast("100", 0), 100)
        self.assertEqual(AKConfig.Cast("True", True), True)
        self.assertEqual(AKConfig.Cast('{"key": "value"}', {}), {"key": "value"})
        self.assertEqual(AKConfig.Cast("item1,item2", []), ["item1", "item2"])

    def test_create_table(self):
        entries = {"key1": "value1", "key2": "value2"}
        table = AKConfig.CreateTable(entries, title="Test Table")
        self.assertIn("Test Table", table)
        self.assertIn("key1", table)
        self.assertIn("value1", table)

    def test_get_globals(self):
        globals_list = AKConfig.GetGlobals(self.global_vars)
        self.assertIn("string_var", globals_list)
        self.assertIn("int_var", globals_list)
        self.assertNotIn(
            "__builtins__", globals_list
        )  # Ensure built-in vars are not included

    def test_masking(self):
        masked_config = self.ak_config.get_config(mask_length=3)
        self.assertEqual(masked_config["string_var"], "***")

    def tearDown(self):
        # Clean up any environment variables if needed
        pass


if __name__ == "__main__":
    unittest.main()
