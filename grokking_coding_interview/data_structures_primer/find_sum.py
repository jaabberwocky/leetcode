def find_sum(lst, k):
    lst.sort()
    start, end = 0, len(lst) - 1
    total = 0

    while total != k:
        if total < k:
            start += 1
        else:
            end -= 1
        total = lst[start] + lst[end]
    return [lst[start], lst[end]]


class Test:

    def test_1(self):
        assert find_sum([1, 21, 3, 14, 5, 60, 7, 6], 81) == [21, 60]
