import unittest

question_05 = """
3-6-9
Given an integer n, return a list with each number from 1 to n, except if it’s a multiple of 3 or has a 3, 6, or 9 in the number, it should be the string “clap”.
Note: return the number as a string.

Example 1:

Input:
n = 16

Output:
[“1”, “2”, “clap”, “4”, “5”, “clap”, “7”, “8”, “clap”, “10”, “11”, “clap”, “clap”, “14”, “clap”, “clap”]

Explanation:
- 3, 6, 9, 12, and 15 are replaced by “clap” since they are divisible by 3.
- 13 is replaced since it has a 3 in the number.
- 16 is replaced since it has a 6 in the number.
"""


# Implement the below function and run the program

def clap_number(n):
    string = "clap"
    ls=[str(i) for i in range(1,n+1)]
    for i in range(len(ls)):
         if int(ls[i])%3==0:
            ls[i]=string
         elif '3' in ls[i]:
            ls[i]=string
         elif '6' in ls[i]:
            ls[i]=string
         elif '9' in ls[i]:
            ls[i]=string
    return ls
    


class TestClapNumber(unittest.TestCase):

    def test_1(self):
        self.assertEqual(clap_number(5), ["1", "2", "clap", "4", "5"]
                         )

    def test_2(self):
        self.assertEqual(clap_number(16), ["1", "2", "clap", "4", "5", "clap",
                                           "7", "8", "clap", "10", "11", "clap", "clap", "14", "clap", "clap"])

    def test_3(self):
        self.assertEqual(clap_number(39), ["1", "2", "clap", "4", "5", "clap", "7", "8", "clap", "10", "11", "clap", "clap", "14", "clap", "clap", "17", "clap", "clap", "20", "clap",
                                           "22", "clap", "clap", "25", "clap", "clap", "28", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "clap"])

    def test_4(self):
        self.assertEqual(clap_number(512), ["1", "2", "clap", "4", "5", "clap", "7", "8", "clap", "10", "11", "clap", "clap", "14", "clap", "clap", "17", "clap", "clap", "20", "clap", "22", "clap", "clap", "25", "clap", "clap", "28", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "40", "41", "clap", "clap", "44", "clap", "clap", "47", "clap", "clap", "50", "clap", "52", "clap", "clap", "55", "clap", "clap", "58", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "70", "71", "clap", "clap", "74", "clap", "clap", "77", "clap", "clap", "80", "clap", "82", "clap", "clap", "85", "clap", "clap", "88", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "100", "101", "clap", "clap", "104", "clap", "clap", "107", "clap", "clap", "110", "clap", "112", "clap", "clap", "115", "clap", "clap", "118", "clap", "clap", "121", "122", "clap", "124", "125", "clap", "127", "128", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "140", "clap", "142", "clap", "clap", "145", "clap", "clap", "148", "clap", "clap", "151", "152", "clap", "154", "155", "clap", "157", "158", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "170", "clap", "172", "clap", "clap", "175", "clap", "clap", "178", "clap", "clap", "181", "182", "clap", "184", "185", "clap", "187", "188", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "200", "clap", "202", "clap", "clap", "205", "clap", "clap", "208", "clap", "clap", "211", "212", "clap", "214", "215", "clap", "217", "218", "clap", "220", "221", "clap", "clap", "224", "clap", "clap", "227", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "241", "242", "clap", "244", "245", "clap", "247", "248", "clap", "250", "251", "clap", "clap", "254", "clap", "clap", "257", "clap", "clap",
                                            "clap", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "271", "272", "clap", "274", "275", "clap", "277", "278", "clap", "280", "281", "clap", "clap", "284", "clap", "clap", "287", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "400", "401", "clap", "clap", "404", "clap", "clap", "407", "clap", "clap", "410", "clap", "412", "clap", "clap", "415", "clap", "clap", "418", "clap", "clap", "421", "422", "clap", "424", "425", "clap", "427", "428", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "440", "clap", "442", "clap", "clap", "445", "clap", "clap", "448", "clap", "clap", "451", "452", "clap", "454", "455", "clap", "457", "458", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "470", "clap", "472", "clap", "clap", "475", "clap", "clap", "478", "clap", "clap", "481", "482", "clap", "484", "485", "clap", "487", "488", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "clap", "500", "clap", "502", "clap", "clap", "505", "clap", "clap", "508", "clap", "clap", "511", "512"])


if __name__ == '__main__':
    unittest.main(verbosity=2)
