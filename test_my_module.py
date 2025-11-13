# test_my_module.py
import unittest
from my_module import simple_math, get_data
from unittest.mock import patch, Mock

class TestMyModule(unittest.TestCase):

    def test_simple_math(self):
        # Test a basic function to ensure unit tests run successfully [cite: 21]
        self.assertEqual(simple_math(2, 3), 5)

    # Mocking the network call so the test doesn't depend on external sites
    @patch('my_module.requests.get')
    def test_get_data_success(self, mock_get):
        # Configure the mock response
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.text = "This is some test data that is successfully fetched."
        mock_get.return_value = mock_response

        # Call the function
        result = get_data("http://test.com")

        # Assertions
        self.assertIn("This is some test data", result)
        mock_get.assert_called_once_with("http://test.com", timeout=5)

if __name__ == '__main__':
    unittest.main()
