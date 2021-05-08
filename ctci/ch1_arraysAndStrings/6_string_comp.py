import unittest


def string_compression(s: str) -> str:
    comp_string = ""
    current_ch = s[0]
    current_count = 0

    for ch in s:
        if ch != current_ch:
            comp_string += str(current_ch) + str(current_count)
            current_ch = ch
            current_count = 1
        else:
            current_count += 1
    # add the last combination at end of string
    comp_string += str(current_ch) + str(current_count)

    if len(comp_string) < len(s):
        return comp_string
    else:
        return s


class Test(unittest.TestCase):

    def test_1(self):
        s = "aabcccccaa"
        self.assertEqual(string_compression(s), "a2b1c5a2")

    def test_2(self):
        s = "abcd"
        self.assertEqual(string_compression(s), "abcd")