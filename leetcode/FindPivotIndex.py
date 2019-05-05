class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return -1
    
        sumLeft = 0
        sumRight = 0
        totalSum = sum(nums)
        
        for ind, val in enumerate(nums):
            sumRight = totalSum - val - sumLeft
            
            if sumLeft == sumRight:
                return ind
            else:
                sumLeft += val
        return -1