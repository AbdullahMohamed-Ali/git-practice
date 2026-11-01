
import unittest

from calculator import sum_numbers


class TestCalculator(unittest.TestCase):


    def test_addition_positive_numbers(self):
        self.assertEqual(sum_numbers(5, 3), 8)

    def test_addition_negative_numbers(self):
        self.assertEqual(sum_numbers(-5, -3), -8)

