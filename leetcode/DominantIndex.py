class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        
        maxNum = 0
        maxInd = 0
        
        for ind, val in enumerate(nums):
            if val > maxNum:
                maxNum = val
                maxInd = ind
        
        sortNums = sorted(nums)[:-1]
        if (maxNum / 2) >= sortNums[-1]:
            return maxInd
        else:
            return -1