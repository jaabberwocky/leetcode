class Solution:
    def plusOne(self, digits):
        digitString = "".join([str(d) for d in digits])
        finalDigits = int(digitString) + 1
        return [int(d) for d in str(finalDigits)]