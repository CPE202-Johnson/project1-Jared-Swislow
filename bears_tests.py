import unittest
from bears import *

class TestAssign1(unittest.TestCase):
    #Testing for values that should return true
    def test_bear_true(self):
        self.assertTrue(bears(250))
        self.assertTrue(bears(42))
        self.assertTrue(bears(210))
        self.assertTrue(bears(5280))

    #Testing for values that should return false
    def test_bear_false(self):
        self.assertFalse(bears(53))
        self.assertFalse(bears(41))
        self.assertFalse(bears(300))
        self.assertFalse(bears(0))
    
    #Error checking
    def test_bear_errors(self):
        with self.assertRaises(ValueError):
            bears(-3)
        with self.assertRaises(ValueError):
            bears("bears")

if __name__ == "__main__":
    unittest.main()
