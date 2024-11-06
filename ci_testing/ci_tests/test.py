# tests

import unittest

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

class TestMathFunctions(unittest.TestCase):  
    def test_add(self):
        self.assertEqual(add(2, 3), 4)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)

    def test_multiply(self):
        self.assertEqual(multiply(4, 3), 12)

if __name__ == '__main__':
    unittest.main()
