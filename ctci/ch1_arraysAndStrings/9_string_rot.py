import unittest


def is_rotated_string(s1: str, s2: str) -> bool:
    return s2 in s1+s1

class Test(unittest.TestCase):

    def test_1(self):
        s1, s2 = "erbottlewat", "waterbottle"
        self.assertTrue(is_rotated_string(s1,s2))

    def test_2(self):
        s1, s2 = "james", "bond"
        self.assertFalse(is_rotated_string(s1,s2))

    def test_3(self):
        s1, s2 = "melonwater", "watermelon"
        self.assertTrue(is_rotated_string(s1,s2))