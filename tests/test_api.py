import unittest.mock
from Calc.api_mock import *


class MyTestCase(unittest.TestCase):
    def test_get_only_numbers(self):
        test_data = ["1", "2", "3", "25", "36a", "37", "a1", "asdfasdf", "14", "18"]
        expected_data = "1|2|3|25|37|14|18"
        fake_api = unittest.mock.MagicMock()  # sukuriam object fake
        fake_api.get_data.return_value = test_data  # priskiriam testdata kaip musu funkcijos get_data return_value
        with unittest.mock.patch('Calc.api_mock.API', fake_api):
            result = get_only_numbers()
            self.assertEqual(result, expected_data)
