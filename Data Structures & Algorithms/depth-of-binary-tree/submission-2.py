# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        maxdepth = 1
        def dfs(node, depth):
            nonlocal maxdepth
            if not node:
                maxdepth = max(maxdepth, depth)
                return maxdepth

            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)

        dfs(root, 0)
        return maxdepth

        # maxdepth = 1
        # stack = [(root, 1)]
        # while stack:
        #     node, depth = stack.pop()
        #     if not node.left and not node.right:
        #         maxdepth = max(depth, maxdepth)
        #         continue
        #     if node.right:
        #         stack.append((node.right, depth + 1))
        #     if node.left:
        #         stack.append((node.left, depth + 1))

        # return maxdepth
            
