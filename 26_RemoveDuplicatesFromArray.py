#URL: https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # guarantee that sorted
        nums.sort()
        
        for i, n in enumerate(nums):
            try:
                while True:
                    if n == nums[i + 1]:
                        nums.pop(i + 1)
                    else:
                        break
                        
            # for index out of bounds (last item)
            except:
                pass
            
        return len(nums)