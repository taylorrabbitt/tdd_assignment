''' 
input: [1, 2, 3, 4, 5, 6, 18, 15]
output: ['1', '2', 'fizz', '4', 'buzz', 'fizz', 'fizz', 'fizzbuzz'] '''


import unittest
from product import *

class TestProduct(unittest.TestCase):
	def testProcessNums(self):
		prod = Product()

		''' base cases '''
		self.assertEqual(prod.processNums("",""), "", "should not return a number if the input strings do not include numbers")
		self.assertEqual(prod.processNums("12", ""), 12, "should return num1 if num2 is an empty string")
		self.assertEqual(prod.processNums("", "12"), 12, "should return num2 if num1 is an empty string")
		self.assertEqual(prod.processNums("0", "15"), 0, "should return 0 if either num1 or num2 is '0'")
		self.assertEqual(prod.processNums("15", "0"), 0, "should return 0 if either num1 or num2 is '0'")
		self.assertEqual(prod.processNums('1', 1), 'Error', "should return 'Error' if either num1 or num2 is not a string")
		self.assertEqual(prod.processNums(1, '1'), 'Error', "should return 'Error' if either num1 or num2 is not a string")
		
		''' normal functionality '''
		self.assertEqual(prod.processNums("1","1"), 1, "should return 1 if given num1 = '1' and num2 = '1'")
		self.assertEqual(prod.processNums("10", "2"), 20, "should return 10 if given num1 = '10' and  num2 = '2'")
		self.assertEqual(prod.processNums("100", "15"), 1500, "should return 1500 if given num1 = '100' and num2 = '15'")
		self.assertEqual(prod.processNums("1234", "18"), 22212, "should return 22212 if given num1 = '1234' and num2 = '18'")

if __name__ == "__main__":
	unittest.main()
