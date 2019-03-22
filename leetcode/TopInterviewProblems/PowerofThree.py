class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        num = 0
        power = 0
        
        while power < n:
            power = 3 ** num
            if power == n:
                return True
            else:
                num += 1
        return False