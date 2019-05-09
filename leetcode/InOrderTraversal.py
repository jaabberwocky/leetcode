# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        visited = []
        done = Solution.traverse(root, visited)
        return done
    
    @staticmethod
    def traverse(root, visited):
        if root is None:
            return visited
        if root.left is not None:
            Solution.traverse(root.left, visited)
        visited.append(root.val)
        if root.right is not None:
            Solution.traverse(root.right, visited)
        return visited