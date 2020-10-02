import unittest

question_01 = """
Given a query string s and a list of all possible words, return all words that have s as a prefix.

Example 1:

Input:
s = “de”
words = [“dog”, “deal”, “deer”]

Output:
[“deal”, “deer”]

Explanation:
Only deal and deer begin with de.

Example 2:

Input:
s = “b”
words = [“banana”, “binary”, “carrot”, “bit”, “boar”]

Output:
[“banana”, “binary”, “bit”, “boar”]

Explanation:
All these words start with b, except for “carrot”.
"""

# Implement the below function and run the program


def prefix_words(prefix, words):
    n=len(prefix)
    Res=  [i for i in words if i[:n] == prefix] 
    return Res


class TestPrefixWords(unittest.TestCase):

    def test_1(self):
        self.assertEqual(prefix_words(
            'de', ['dog', 'deal', 'deer']), ['deal', 'deer'])

    def test_2(self):
        self.assertEqual(prefix_words(
            'b', ['banana', 'binary', 'carrot', 'bit', 'boar']), ['banana', 'binary', 'bit', 'boar'])


if __name__ == '__main__':
    unittest.main(verbosity=2)
