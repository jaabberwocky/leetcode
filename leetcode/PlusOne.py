class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        return [int(x) for x in str((int("".join([str(x) for x in digits])) + 1))]