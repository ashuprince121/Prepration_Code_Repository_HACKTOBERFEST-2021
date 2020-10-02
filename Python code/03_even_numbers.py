# Even numbers

"""
Given a 2-dimensional list matrix, return the number of even numbers in the 
matrix.

Example 1
Input

matrix = [[1, 2, 8],
[3, 5, 5],
[4, 6, 6]]
Output

5
Explanation

The even numbers are: 2, 8, 4, 6, and 6.
"""

# solution

import unittest


def even_numbers(matrix):
    count = 0
    for i in matrix:
        for j in i:
            if j % 2 == 0:
                count += 1
    return count

# DO NOT TOUCH THE BELOW CODE


class TestEvenNumbers(unittest.TestCase):
    def test_01(self):
        self.assertEqual(even_numbers([[1, 2, 8], [3, 5, 5], [4, 6, 6]]), 5)

    def test_02(self):
        self.assertEqual(even_numbers([[1], [2], [4]]), 2)

    def test_03(self):
        self.assertEqual(even_numbers([[1, 2, 3]]), 1)


if __name__ == '__main__':
    unittest.main(verbosity=2)
