# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from math import inf
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        def f(root,M):
            if not root: return
            if root.val >= M:
                nonlocal res; res += 1
            M = max(M, root.val)
            f(root.left,M); f(root.right, M)
        f(root,-inf)
        return res