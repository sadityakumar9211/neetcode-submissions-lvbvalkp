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
        
        queue = collections.deque([(root, 1)])
        max_d = 1
        while queue:
            node, d = queue.popleft()
            max_d = max(max_d, d)
            if node.right:
                queue.append((node.right, d+1))    
            if node.left:
                queue.append((node.left, d+1))
        
        return max_d
