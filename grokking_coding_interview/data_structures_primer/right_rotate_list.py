def right_rotate(lst, k):
    if not lst:
        return lst
    i = 1
    while i <= k:
        val = lst.pop()
        lst.insert(0, val)
        i += 1
    return lst


class Test:

    def test_1(self):
        assert right_rotate(['right', 'rotate', 'python'], 4) == ['python', 'right', 'rotate']
