class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        digits = [int(x) for x in str(n)]
        prod = 0
        summed = 0
        
        for ind, d in enumerate(digits):
            if ind == 0:
                prod = d
            else:
                prod *= d
            summed += d
        
        return prod - summed