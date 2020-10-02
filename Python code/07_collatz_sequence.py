# Collatz sequence

"""
Given a positve integer n, find the length of its Collatz sequence.
Collatz sequence is generated sequentially where

n = n / 2 if n is even
n = 3 * n + 1 if n is odd
And the sequence ends if n = 1
Example 1
Input

n = 11
Output

15
Explanation

The Collatz sequence is:
[11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
and its length is 15.
"""

# solution

import unittest



def collatz_sequence(n):
    count = 0
    while n > 0:
        if n == 1:
            return count+1
        else:
            count += 1
            if n % 2 == 0:
                n = n/2
            else:
                n = n*3+1


class TestCollatzSequence(unittest.TestCase):
    def test_1(self):
        self.assertEqual(collatz_sequence(11), 15)

    def test_2(self):
        self.assertEqual(collatz_sequence(1), 1)

    def test_3(self):
        self.assertEqual(collatz_sequence(2), 2)


if __name__ == '__main__':
    unittest.main(verbosity=2)
