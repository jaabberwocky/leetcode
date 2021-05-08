import unittest


class Solution:
    @staticmethod
    def check_permutation(s1: str, s2: str) -> bool:
        """
        Check if string s1 is a permutation of s2.

        Definition of permutation:
            1. Has all the same characters
            2. Has same length
        :param s1: String
        :param s2: String
        :return: True if s1 is a permutation of s2 and vice versa.
        """
        if len(s1) != len(s2):
            return False
        else:
            d1 = dict()
            d2 = dict()

            for i in range(len(s1)):
                if s1[i] not in d1:
                    d1[s1[i]] = 1
                elif s1[i] in d1:
                    d1[s1[i]] += 1

                if s2[i] not in d2:
                    d2[s2[i]] = 1
                elif s2[i] in d2:
                    d2[s2[i]] += 1

            for k, v in d1.items():
                try:
                    if d2[k] != v:
                        return False
                except KeyError:
                    # key not found!
                    return False
        return True


class Test(unittest.TestCase):

    def test_1(self):
        s1, s2 = "", ""
        self.assertEqual(Solution.check_permutation(s1, s2), True)

    def test_2(self):
        s1, s2 = "abc", "bac"
        self.assertEqual(Solution.check_permutation(s1, s2), True)

    def test_3(self):
        s1, s2 = "abcd", "bac"
        self.assertEqual(Solution.check_permutation(s1, s2), False)

    def test_4(self):
        s1, s2 = "a", "aaaa"
        self.assertFalse(Solution.check_permutation(s1, s2))

    def test_5(self):
        s1, s2 = "bbb", "bbb"
        self.assertTrue(Solution.check_permutation(s1,s2))
