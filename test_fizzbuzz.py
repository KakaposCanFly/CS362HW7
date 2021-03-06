import unittest
import fizzbuzz

class Testing(unittest.TestCase):
    def test_test1(self):
        for i in [3, 6, 12, 21]:
            self.assertEqual(fizzbuzz.fizz_buzz(i), "Fizz")

    def test_test2(self):
        for i in [5, 10, 20, 25]:
            self.assertEqual(fizzbuzz.fizz_buzz(i), "Buzz")

    def test_test3(self):
        for i in [15, 30, 45, 60]:
            self.assertEqual(fizzbuzz.fizz_buzz(i), "FizzBuzz")

    def test_test4(self):
        self.assertEqual(fizzbuzz.fizz_buzz(17), 17)

if __name__ == "__main__":
    unittest.main()