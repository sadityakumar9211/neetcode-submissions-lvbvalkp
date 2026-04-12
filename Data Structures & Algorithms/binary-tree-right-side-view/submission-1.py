# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
            
        hashset = {} # depth -> node
        queue = collections.deque([(root, 0)])
        while queue:
            node, depth = queue.popleft()
            hashset[depth] = node.val  # replace the previous value if nothing is present
            if node.left:
                queue.append((node.left, depth+1))
            if node.right:
                queue.append((node.right, depth+1))
    
        return list(hashset.values())