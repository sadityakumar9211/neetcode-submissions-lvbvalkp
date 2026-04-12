"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node
        cloned = {node: Node(node.val)}  # node -> cloned node
        # nodes which have been cloned but neighbours not visited yet!
        queue = collections.deque([node])

        while queue:
            curr = queue.popleft()
            if curr.neighbors:
                for nei in curr.neighbors:
                    if nei not in cloned:
                        cloned[nei] = Node(nei.val)
                        queue.append(nei)
                    
                    cloned[curr].neighbors.append(cloned[nei])
        
        return cloned[node]

