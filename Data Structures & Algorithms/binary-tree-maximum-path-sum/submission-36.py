# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = root.val
        def f(root):
            if not root: return 0
            L,R = max(0,f(root.left)),max(0,f(root.right))
            nonlocal res; res = max(res, root.val + L + R)
            return root.val + max(L,R)
        f(root)
        return res