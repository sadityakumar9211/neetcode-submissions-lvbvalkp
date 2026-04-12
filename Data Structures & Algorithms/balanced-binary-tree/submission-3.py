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
        
        def height(root):
            if not root:
                return 0, True
            
            left, isleft = height(root.left)
            right, isright = height(root.right)

            if not isleft or not isright or abs(right - left) > 1:
                return 0, False
            
            return 1 + max(left, right), True
        
        _, isBalanced = height(root)
        return isBalanced