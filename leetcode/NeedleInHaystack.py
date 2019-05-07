class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == '':
            return 0
        elif haystack == '':
            return -1
        elif needle not in haystack:
            return -1
        else:
            return haystack.find(needle)