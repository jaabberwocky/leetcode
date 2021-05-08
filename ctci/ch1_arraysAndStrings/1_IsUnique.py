import unittest


class Solution:
    @staticmethod
    def isUnique(s):
        """
        Returns true if string contains all unique characters.
        """
        chars = {}
        for ch in s.lower():
            if ch not in chars:
                chars[ch] = 1
            else:
                return False
        return True


class Test(unittest.TestCase):

    def test_1(self):
        self.assertEqual(Solution.isUnique('abcd'), True)

    def test_2(self):
        self.assertEqual(Solution.isUnique('aaa'), False)

    def test_3(self):
        self.assertEqual(Solution.isUnique('aKvC%4'), True)

    def test_4(self):
        self.assertEqual(Solution.isUnique('aKvC%4a'), False)

    def test_5(self):
        self.assertEqual(Solution.isUnique('4561 '), True)


if __name__ == "__main__":
    unittest.main()
