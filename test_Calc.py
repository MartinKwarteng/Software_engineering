import unittest
import Calc

# Class to inherit unittest 
class TestCalc(unittest.TestCase):
      # Method
    def test_add(self):
        result = Calc.add(2, 1)
        self.assertEqual = (result, 3)
        self.assertEqual = (Calc.add(-2, 3), 1)  # Edge cases 
        self.assertEqual = (Calc.add(-2, -3), -5)


    def test_multiply(self):
        self.assertEqual = (Calc.multiply(10, 10), 100)
        self.assertEqual = (Calc.multiply(-2, 3), -6)  # Edge cases 
        self.assertEqual = (Calc.multiply(-2, -3), 6)
    

    def test_subtract(self):
        self.assertEqual = (Calc.subtract(10, 1), 9)
        self.assertEqual = (Calc.subtract(-2, 5), -7)  # Edge cases 
        self.assertEqual = (Calc.subtract(-2, -3), 1)

    def test_division(self):
        self.assertEqual = (Calc.division(100, 2), 50)
        self.assertEqual = (Calc.division(-2, 1), -2)  # Edge cases 
        self.assertEqual = (Calc.division(-2, -2), 1)
        self.assertEqual = (Calc.division(5, 2), 2.5)

        with self.assertRaises(ValueError): # testing the valueError exception
            Calc.division(2, 0)
              



if __name__ == '__main__':
    unittest.main()


