import unittest


def one_away(s1, s2):
    if s1 == s2:
        return True

    diff = []

    for i in range(len(s1)):
        if s1[i] not in s2:
            diff.append(s1[i])

    return len(diff) <= 1


class Test(unittest.TestCase):

    def test_1(self):
        s1, s2 = "pale", "ple"
        self.assertTrue(one_away(s1, s2))

    def test_2(self):
        s1, s2 = "pales", "pale"
        self.assertTrue(one_away(s1, s2))

    def test_3(self):
        s1, s2 = "pale", "bale"
        self.assertTrue(one_away(s1, s2))

    def test_4(self):
        s1, s2 = "pale", "bake"
        self.assertFalse(one_away(s1, s2))

    def test_5(self):
        s1, s2 = "push", "abcd"
        self.assertFalse(one_away(s1, s2))

    def test_6(self):
        s1, s2 = "" , ""
        self.assertTrue(one_away(s1, s2))

    def test_6(self):
        s1, s2 = "", " "
        self.assertTrue(one_away(s1, s2))
