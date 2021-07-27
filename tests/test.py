import unittest
import os, sys
sys.path.insert(0, os.path.abspath("."))
from src import main

class TestFactorial(unittest.TestCase):
    def test_factorial(self):
        """
        Test that it calculate factorials properly
        """
        
        resultA = main.factorial(0)
        resultB = main.factorial(1)
        resultC = main.factorial(10)
        resultD = main.factorial(6)
        self.assertEqual(resultA, 1)
        self.assertEqual(resultB, 1)
        self.assertEqual(resultC, 3628800)
        self.assertEqual(resultD, 6)
        

if __name__ == '__main__':
    unittest.main()
