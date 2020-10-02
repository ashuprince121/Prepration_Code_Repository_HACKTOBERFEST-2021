
# Odd number of

"""
Given a list of positive integers nums, return the number of integers that
have odd number of digits.

Example 1
Input

nums = [1, 800, 2, 10, 3]
Output

4
Explanation

[1, 800, 2, 3] have odd number of digits.
"""

# solution

import unittest


def odd_number_digits(nums):
    count = 0
    for i in nums:
        s = str(i)
        if len(s)%2 != 0:
            count +=1
    return count



# DO NOT TOUCH THE BELOW CODE

class TestOddNumberDigits(unittest.TestCase):
    def test_01(self):
        self.assertEqual(odd_number_digits([1, 800, 2, 3]), 4)

    def test_02(self):
        self.assertEqual(odd_number_digits([1]), 1)

    def test_03(self):
        self.assertEqual(odd_number_digits([]), 0)


if __name__ == '__main__':
    unittest.main(verbosity=2)
