#URL: https://leetcode.com/problems/two-sum/description/
#Desc: 
'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.
'''
import unittest
class Solution:

    @staticmethod
    def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        # iterate to find pair 
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                summed = nums[i] + nums[j]
                if summed == target:
                    return [nums[i], nums[j]]
        return [None, None]

    @staticmethod
    def twoSumEfficient(nums, target):
        # sort first then use two pointers
        nums.sort()
        
        summed, i, j = 0, 0, len(nums) - 1

        while i < j:
            summed = nums[i] + nums[j]
            if summed == target:
                return [nums[i], nums[j]]
            elif summed < target:
                i += 1
            else:
                j -= 1
        return [None, None]
        
class tests(unittest.TestCase):

    def testTwoSum(self):
        arr = [1,2,3,4,5]
        s = 8
        self.assertEqual(Solution.twoSum(arr,s), [3,5])

    def testTwoSumEfficient(self):
        arr = [1,2,3,4,5]
        s = 8
        self.assertEqual(Solution.twoSumEfficient(arr,s), [3,5])

    def testNone(self):
        arr = [100,200,300]
        s = 8
        self.assertEqual(Solution.twoSumEfficient(arr,s), [None, None])

if __name__ == "__main__":
    unittest.main()