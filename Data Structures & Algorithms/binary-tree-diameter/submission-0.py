# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def height(node):
            if not node:
                return 0
            return 1 + max(height(node.left), height(node.right))

        
        diameter = 0
        def dfs(node):
            nonlocal diameter
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)

            longestPath = left + right
            diameter = max(diameter, longestPath)

            return 1 + max(left, right)
    
        dfs(root)
        return diameter

        