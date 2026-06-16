"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        M = defaultdict(lambda:Node(0))
        M[None] = None
        curr = head
        while curr:
            M[curr].val = curr.val
            M[curr].next = M[curr.next]
            M[curr].random = M[curr.random]
            curr = curr.next
        return M[head]