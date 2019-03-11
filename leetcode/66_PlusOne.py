class Solution:
    def plusOne(self, digits):
        return [int(d) for d in str(int("".join([str(d) for d in digits])) + 1)]