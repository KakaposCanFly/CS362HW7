import unittest


class Testing(unittest.TestCase):
    def test_leapYear(self):
        self.assertTrue(leapyear.is_leap_year(2004))


if __name__ == "__main__":
    unittest.main()