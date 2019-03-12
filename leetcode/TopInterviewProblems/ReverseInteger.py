class Solution:
    def reverse(self, x: int) -> int:
        isPositive = x >= 0
        reversed = int(str(abs(x))[::-1])
        
        if reversed > 2**31:
            # check for overflow
            return 0
        
        if isPositive == False:
            return -reversed
        else:
            return reversed