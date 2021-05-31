import unittest

class Testing(unittest.TestCase):
    def test_test1(self):
        for i in [3, 6, 12, 21]:
            self.assertEqual(fizzbuzz.fizz_buzz(i), "Fizz")

if __name__ == "__main__":
    unittest.main()