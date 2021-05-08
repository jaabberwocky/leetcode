import unittest
from typing import List


def rotate_matrix(m: List) -> List:
    i = 0
    n = len(m)
    rot_m = []
    while i < n:
        row = []
        j = n - 1
        while j >= 0:
            row.append(m[j][i])
            j -= 1
        i += 1
        rot_m.append(row)
    return rot_m


class Test(unittest.TestCase):

    def test_1(self):
        m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(rotate_matrix(m), [[7, 4, 1], [8, 5, 2], [9, 6, 3]])
