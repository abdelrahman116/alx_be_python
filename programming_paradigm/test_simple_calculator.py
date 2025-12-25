import unittest 
from simple_calculator import SimpleCalculator
class Claculator_Test(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()
    def test_addition(self):
        self.assertEqual(self.calc.add(self,5,5),10)
    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(self,5,5),0)
    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(self,5,5),25)
    def test_divide_normal(self):
        self.assertEqual(self.calc.divide(self,5,5),1)
    def test_divide_zero(self):
        self.assertEqual(self.calc.divide(self,5,0),None)


if __name__ == "__main__":
    unittest.main()