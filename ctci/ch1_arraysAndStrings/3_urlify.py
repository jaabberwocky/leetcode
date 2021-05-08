import unittest


class Solution:
    @staticmethod
    def urlify(s1: str, true_length: int) -> str:
        """
        Replaces all spaces with '%20' of a string up to its true length (true_length).
        :param s1: String
        :param true_length: True length of string
        :return: Edited string
        """
        trimmed_str = s1[:true_length]
        return trimmed_str.replace(" ", "%20")


class Test(unittest.TestCase):

    def test_1(self):
        self.assertEqual(Solution.urlify("Mr John Smith    ", 13), "Mr%20John%20Smith")

    def test_2(self):
        s1 = ""
        self.assertEqual(Solution.urlify(s1, 0), "")
