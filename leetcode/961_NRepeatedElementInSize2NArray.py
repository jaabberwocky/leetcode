class Solution:
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        requiredLength = len(A)/2
        counter = {}

        for i in A:
            if i not in counter:
                counter[i] = 1
            else:
                return i
