import unittest
from itertools import permutations

question_04 = """
Rotating primes

Given an integer n, return whether every rotation of n is prime.
Example 1:
Input:
n = 199
Output:
True
Explanation:
199 is prime, 919 is prime, and 991 is prime.

Example 2:
Input:
n = 19
Output:
False
Explanation:
Although 19 is prime, 91 is not.
"""


# Implement the below function and run the program 
def nod(n): 
    c=0
    while n>0: 
        c=c+1
        n=n//10
    return c 
def isPrime(n):
    for i in range(2,int(n*0.5)):
        if n%i==0:
            return False
    return True
def is_rotating_prime(num):
     digit = nod(num) 
     pow_of_ten = pow(10,digit - 1)
     if digit>1:
        for i in range(digit - 1):
            firstDigit = num // pow_of_ten  
            left = (num * 10 + firstDigit - 
               (firstDigit * pow_of_ten * 10))   
            num = left
            return isPrime(num)
     else:
        return isPrime(num)
  
        
class TestIsRotatingPrime(unittest.TestCase):

    def test_1(self):
        self.assertEqual(is_rotating_prime(2), True)

    def test_2(self):
        self.assertEqual(is_rotating_prime(199), True)

    def test_3(self):
        self.assertEqual(is_rotating_prime(19), False)

    def test_4(self):
        self.assertEqual(is_rotating_prime(791), False)

    def test_5(self):
        self.assertEqual(is_rotating_prime(919), True)


if __name__ == '__main__':
    unittest.main(verbosity=2)
