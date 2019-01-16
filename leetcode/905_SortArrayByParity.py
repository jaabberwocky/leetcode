class Solution:
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        evenList = [x for x in A if x % 2 == 0]
        oddList = [y for y in A if y % 2 != 0]
        return evenList + oddList