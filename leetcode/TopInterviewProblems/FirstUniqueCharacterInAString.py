class Solution:
    def firstUniqChar(self, s: str) -> int:
        # construct character counts
        d = {}
        for ch in s:
            if ch not in d:
                d[ch] = 1
            else:
                d[ch] += 1
        
        # find the first character with only one occurrence
        for ind, ch in enumerate(s):
            if d[ch] == 1:
                return ind
        return -1
        