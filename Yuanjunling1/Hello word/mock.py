import mock
import unittest
class MyTestCase(unittest.TestCase):
    @mock.patch('multiply')
    def test_add_multiply(mock_multiply):
        x=3
        x=5
        mock_multiply.return_value=15
        addition,multiply = add_and_multipy(x,y)
        mock_multiply.assert_called_once_with(3, 5)
        self.assertEqual(8, addition)
        self.assertEqual(15, multiple)
if __name__ == "__main__":
    unittest.main()



