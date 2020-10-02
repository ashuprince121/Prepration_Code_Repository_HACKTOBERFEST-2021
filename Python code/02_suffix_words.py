import unittest

question_02 = """
Given a query string s and a list of all possible words,
return all words that have s as a suffix.

Example 1:
Input:
s = “ed”
words = [“called”, “aged”, “land”]

Output:
[“called”, “aged”]

Explanation:
Only called and aged ends with ed.

Example 2:
Input:
s = “d”
words = [“helped”,  “held”, “land”, “mat”, “cat”, “bold”]

Output:
[“helped”,  “held”, “land”, “bold”]

Explanation:
All these words ends with d, except for “mat” and “cat”.
"""

# Implement the below function and run the program


def suffix_words(suffix, words):
    n=len(suffix)
    Res=  [i for i in words if i[-n:] == suffix] 
    return Res


class TestSuffixWords(unittest.TestCase):

    def test_1(self):
        self.assertEqual(suffix_words(
            'ed', ['called', 'aged', 'land']), ['called', 'aged'])

    def test_2(self):
        self.assertEqual(suffix_words(
            'd', ['helped', 'held', 'land', 'mat', 'cat', 'bold']), ['helped', 'held', 'land', 'bold'])


if __name__ == '__main__':
    unittest.main(verbosity=2)
