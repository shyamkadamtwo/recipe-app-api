# write simple testcase
from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):
    '''Test the calc module.'''

    def test_add_numbers(self):
        """Test adding number"""
        res = calc.add(5, 6)
        self.assertEqual(res, 11)

    def test_subtract_number(self):
        """Test subtracting number"""
        res = calc.subtract(4, 7)
        self.assertEqual(res, 3)

