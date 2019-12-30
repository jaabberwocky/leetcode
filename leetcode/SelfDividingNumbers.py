class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        selfDividingNums = []
        for i in range(left,right + 1):
            if '0' in str(i):
                continue
            else:
                digits = [int(d) for d in list(str(i))]
                isNotSelfDividing = False
                for d in digits:
                    if i % d == 0:
                        continue
                    else:
                        isNotSelfDividing = True
                        break
                if isNotSelfDividing == False:
                    selfDividingNums.append(i)
        return selfDividingNums