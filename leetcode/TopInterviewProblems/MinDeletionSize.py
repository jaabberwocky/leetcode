class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        numCols = len(A[0])
        indices = 0
        
        for i in range(numCols):
            if Solution.isColSorted(A, i) == False:
                indices += 1
        return indices
        
    @staticmethod
    def isColSorted(A: List[str], ind) -> bool:
        col = []
        for i in A:
            col.append(i[ind])
        for ind, j in enumerate(col):
            if ind == 0:
                next
            else:
                if j < col[ind-1]:
                    return False
        return True
    