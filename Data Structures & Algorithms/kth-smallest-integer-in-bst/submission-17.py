# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = 0
        def f(root):
            if not root: return
            f(root.left)
            nonlocal k, res
            k -= 1
            if k == 0:
                res = root.val
                return
            f(root.right)
        f(root)
        return res