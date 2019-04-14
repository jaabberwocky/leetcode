class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            dictS = Solution.getCount(s)
            dictT = Solution.getCount(t)
            return dictS == dictT
            
    
    @staticmethod
    def getCount(s):
        d = {}
        for i in s:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        return d