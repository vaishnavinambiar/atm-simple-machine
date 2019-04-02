import unittest
import sys
from atm8 import pin_number
from atm8 import getPin
from atm8 import options
from atm8 import getContinued

class MyTest(unittest.TestCase):
    def test_one(self):
         pin_one = '1234'
         pin_two = '1234'
         self.assertEqual(pin_one, pin_two)

    def test_two(self):
        pin_three = '1234'
        pin_four = '2345'
        self.assertNotEqual(pin_three, pin_four)
        
    def test_three(self):
        balance = 50000
        withdraw = 5000
        available_balance = balance - withdraw
        self.assertNotEqual(available_balance, 40000)

    def test_four(self):
        balance = 50000
        withdraw = 5000
        available_balance = balance - withdraw
        self.assertTrue(True, 45000)

    def test_five(self):
        old_pin = '1234'
        new_pin = '4536'
        self.assertEqual(old_pin, new_pin)

if __name__== '__main__':
    unittest.main()
