"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return None
        M = {node: Node(node.val)}
        M[None] = None
        Q = deque([node])
        while Q:
            u = Q.popleft()
            for v in u.neighbors:
                if v not in M:
                    M[v] = Node(v.val)
                    Q.append(v)
                M[u].neighbors.append(M[v])
        return M[node]