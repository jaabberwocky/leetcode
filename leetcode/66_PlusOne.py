class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        reversedArr = digits[::-1]
        for ind, num in enumerate(reversedArr):
            reversedArr[ind] += 1
            if reversedArr[ind] >= 10:
                reversedArr[ind] = 0
                if ind == len(reversedArr) - 1:
                    # last item, we need to insert one at the head
                    reversedArr.append(1)
                    break
            else:
                break
        return reversedArr[::-1]