import unittest
import os, sys
from functools import cache
sys.path.insert(0, os.path.abspath("."))
from src import math as m

class TestFactorial(unittest.TestCase):
    def test_factorial(self):
        """
        Test that it calculate factorials properly
        """
        
        self.assertEqual(m.factorial(0), 1)
        self.assertEqual(m.factorial(1), 1)
        self.assertEqual(m.factorial(10), 3628800)
        self.assertEqual(m.factorial(6), 720)
        
    def test_fibonacci(self):
        """
            test that it is properly calculating nth fibonacci number
        """ 
        self.assertEqual(m.fibonacci(0), 0)
        self.assertEqual(m.fibonacci(1), 1)
        self.assertEqual(m.fibonacci(35), 9_227_465)
        self.assertEqual(m.fibonacci(50), 12_586_269_025)

if __name__ == '__main__':
    unittest.main()
