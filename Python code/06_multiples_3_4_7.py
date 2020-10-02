"""
# Multiples of 3, 4, 7

If we list all positive integers 10 or below that are multiples of
3, 4, or 7 we get: [3, 4, 6, 7, 8, 9]. The sum of the list is 37.

Given a positive integer n, return the sum of all numbers
less than or equal to n that are multiples of 3, 4, or 7.

Example 1
Input

n = 7
Output

20
Explanation

The solution includes [3, 4, 6, 7] and its sum is 20.
"""


import unittest


def multiples_3_4_7(num):
    s=0
    for i in range(1,num+1):
        if i%3==0 or i%4==0 or i%7==0:
            s=s+i
    return s

# DO NOT TOUCH THE BELOW CODE


class TestMultiples_3_4_7(unittest.TestCase):

    def test_01(self):
        input_num = 10
        output_num = 37

        self.assertEqual(multiples_3_4_7(input_num), output_num)

    def test_02(self):
        input_num = 7
        output_num = 20

        self.assertEqual(multiples_3_4_7(input_num), output_num)

    def test_03(self):
        input_num = 1
        output_num = 0

        self.assertEqual(multiples_3_4_7(input_num), output_num)

    def test_04(self):
        input_num = 20
        output_num = 132

        self.assertEqual(multiples_3_4_7(input_num), output_num)


if __name__ == '__main__':
    unittest.main(verbosity=2)
