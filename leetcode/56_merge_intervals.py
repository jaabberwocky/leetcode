# https://leetcode.com/problems/merge-intervals/
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort in place by first element
        intervals.sort(key=lambda x: int(x[0]))

        overlap = []
        non_overlap = []
        interval_count = 1

        lo, hi = intervals[0][0], intervals[0][1]
        for ind, interval in enumerate(intervals):
            if ind == 0:
                continue

            if hi < interval[0]:
                # not an overlapping interval
                if interval_count == 1:
                    # only one interval
                    non_overlap.append([lo, hi])
                else:
                    overlap.append([lo, hi])
                interval_count = 1
                lo, hi = interval[0], interval[1]
            elif hi > interval[1]:
                # not always strictly increasing
                interval_count += 1
            else:
                hi = interval[1]
                interval_count += 1

        # for last item
        if interval_count == 1:
            non_overlap.append([lo, hi])
        else:
            overlap.append([lo, hi])

        return overlap + non_overlap
