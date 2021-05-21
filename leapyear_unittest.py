import unittest
import LeapYear

class leapyear_test(unittest.TestCase):

    def test_leap_pass(self):
        temp = LeapYear.leap_year(2000)
        self.assertEqual(temp,1)

    def test_leap_pass_2(self):
        temp = LeapYear.leap_year(2004)
        self.assertEqual(temp,1)

    def test_leap_fail(self):
        temp = LeapYear.leap_year(2001)
        self.assertEqual(temp,1)


if __name__ == "__main__":
    main()
