# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        ## Drawing the tree for this case is more beneficial --> for each level
        ## To actually see what's happening because its much more, than just invert
        ## Too many duplicate things happenings

        ## Every internal node has its left and right child swapped from top to bottom
        if not root:
            return root
        stack = [root]

        while stack:
            node = stack.pop()
            node.left, node.right = node.right, node.left
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        
        return root

