import unittest
import leapyear

class Testing(unittest.TestCase):
    def test_leapYear(self):
        self.assertTrue(leapyear.is_leap_year(2004))

    def test_leapYear2(self):
        self.assertTrue(leapyear.is_leap_year(2100))


if __name__ == "__main__":
    unittest.main()