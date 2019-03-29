class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        # initialise dictionary
        d = {}
        for ch in t:
            d[ch] = 0
        
        # iterate through using two-pointer method
        right = left = 0
        
        while right < len(s):
            if checkAllCharPresent(d):
                
            
    @staticmethod
    def checkAllCharPresent(d) -> bool:
        for k,v in enumerate(d):
            if v == 0:
                return False
        return True
        