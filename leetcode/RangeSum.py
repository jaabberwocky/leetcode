# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        sum = 0
        curr = root

        while curr.left is not None or curr.right is not None:
            if low <= curr.val <= high:
                sum += curr.val
            else:
                return sum
            if curr.right.val >= low and curr.right.val <= high:
                curr = right
            else:
                curr = left
        return sum


