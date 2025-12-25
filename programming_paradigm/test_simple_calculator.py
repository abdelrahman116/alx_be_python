import unittest 
from simple_calculator import SimpleCalculator
SimpleCalculator()
class Claculator_Test(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(SimpleCalculator.add(self,5,5),10)
    def test_subtract(self):
        self.assertEqual(SimpleCalculator.subtract(self,5,5),0)
    def test_multiply(self):
        self.assertEqual(SimpleCalculator.multiply(self,5,5),25)
    def test_divide_normal(self):
        self.assertEqual(SimpleCalculator.divide(self,5,5),1)
    def test_divide_zero(self):
        self.assertEqual(SimpleCalculator.divide(self,5,0),None)


if __name__ == "__main__":
    unittest.main()