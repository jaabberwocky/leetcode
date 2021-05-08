import unittest


def zero_matrix(m):
    zero_rows = set()
    zero_cols = set()

    # collect distinct rows/cols to be zero-ed
    for i, row in enumerate(m):
        for j, _ in enumerate(row):
            if m[i][j] == 0:
                zero_rows.add(i)
                zero_cols.add(j)

    # apply transformation
    for i, row in enumerate(m):
        for j, _ in enumerate(row):
            if i in zero_rows:
                m[i][j] = 0
            if j in zero_cols:
                m[i][j] = 0

    return m


class Test(unittest.TestCase):

    def test_1(self):
        m = [[1, 2, 3], [4, 5, 6], [7, 0, 9]]
        exp = [[1, 0, 3], [4, 0, 6], [0, 0, 0]]
        self.assertEqual(zero_matrix(m), exp)

    def test_2(self):
        m = [[1, 2, 3], [4, 0, 6], [7, 8, 9]]
        exp = [[1, 0, 3], [0, 0, 0], [7, 0, 9]]
        self.assertEqual(zero_matrix(m), exp)

    def test_3(self):
        # test for general MxN cases
        # test also for more than one zero
        m = [[1, 2, 3, 4], [4, 0, 6, 7], [8, 0, 9, 10]]
        exp = [[1, 0, 3, 4], [0, 0, 0, 0], [0, 0, 0, 0]]
        self.assertEqual(zero_matrix(m), exp)
