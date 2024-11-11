import unittest
from convert import str_to_float

class Testing (unittest.TestCase):

    def test_str_to_float(self):
        word = "314"
        expected = 314.0
        result = str_to_float(314)
        self.assertEqual(expected, result)

    def test_str_to_float2(self):
        word = "31.4"
        expected = 31.4
        result = str_to_float(31.4)
        self.assertEqual(expected, result)

    def test_str_to_float3(self):
        word = "abcd"
        expected = None
        result = str_to_float("abcd")
        self.assertEqual(expected, result)


if __name__ == "__main__":
    unittest.main()