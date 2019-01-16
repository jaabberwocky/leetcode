#URL: https://leetcode.com/problems/two-sum/description/
#Desc: 
'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.
'''

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # remove numbers higher than target
        # nums = [num for num in nums if num < target]
        
        # iterate to find pair 
        for i, num in enumerate(nums):
            paired = target - num
            for j, num_j in enumerate(nums[i+1:]):
                if num_j == paired:
                    return[i, i+j+1]
        