import math


def find_max_sum_sublist(lst):
    local_max, global_max = 0, -math.inf

    for i in range(len(lst)):
        local_max = max(lst[i], lst[i] + local_max)
        if local_max > global_max:
            global_max = local_max

    return global_max


class Test:

    def test_1(self):
        l = [-4, 2, -5, 1, 2, 3, 6, -5, 1]
        assert find_max_sum_sublist(l) == 12
