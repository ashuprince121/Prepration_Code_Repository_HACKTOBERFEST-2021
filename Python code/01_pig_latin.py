# Pig Latin

"""
Given a string s, return a new string where for every word the first character
is moved the end with the suffix "ay" added.

Example 1
Input

s = "hello world"
Output

"ellohay orldway"
"""

import unittest


def pig_latin(s):
    s2 = ''
    for word in s.split():
        s2 = s2 + word[1:] + word[0] + "ay" + " "
    return s2[:len(s2)-1]
# DO NOT TOUCH THE BELOW CODE


class TestPigLatin(unittest.TestCase):
    def test_1(self):
        self.assertEqual(pig_latin(
            "hello world"), "ellohay orldway")

    def test_2(self):
        self.assertEqual(pig_latin(
            "welcom to python"), "elcomway otay ythonpay")


if __name__ == '__main__':
    unittest.main(verbosity=2)
