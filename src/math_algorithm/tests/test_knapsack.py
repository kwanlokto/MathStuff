import unittest

from src.math_algorithm.knapsack import regular_knapsack


class TestKnapsack(unittest.TestCase):
    def test_regular_knapsack(self):
        array = [90, 20, 30, 40, 50, 60, 70, 80, 90]
        self.assertEquals(regular_knapsack(2, array), [0, 8])
