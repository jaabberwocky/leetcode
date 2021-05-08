import unittest


def palindrome_permutation(s: str) -> bool:
    """
    Given a string, write a function to check if it is a permutation of a palindrome.
    A palindrome is a word or phrase that is the same forwards and backwards. A permutation
    is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.
    :param s: String
    :return: True if permutation of palindrome
    """
    s = s.lower()
    d = dict()
    count_of_odd_keys = 0

    for ch in s:
        if ch not in d:
            d[ch] = 1
        else:
            d[ch] += 1

    for k, v in d.items():
        if v % 2 != 0 and k != ' ':
            count_of_odd_keys += 1

    if len(s.replace(' ', '')) % 2 == 0: # remove the spaces for comparison
        return count_of_odd_keys == 0
    else:
        return count_of_odd_keys == 1


class Test(unittest.TestCase):

    def test_1(self):
        s1 = "Tact Coa"
        self.assertTrue(palindrome_permutation(s1))

    def test_2(self):
        s1 = "abbcca"
        self.assertTrue(palindrome_permutation(s1))

    def test_3(self):
        s = "abcd"
        self.assertFalse(palindrome_permutation(s))

    def test_4(self):
        s = "abcd abcd"
        self.assertTrue(palindrome_permutation(s))
