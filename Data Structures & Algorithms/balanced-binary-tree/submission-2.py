# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        isBalanced = True
        # Returns height
        def dfs(node):
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)

            # Update the global variable
            nonlocal isBalanced
            if isBalanced and abs(left - right) > 1:
                isBalanced = False
            
            return 1 + max(left, right)

        dfs(root)
        return isBalanced
