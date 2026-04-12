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

        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root

