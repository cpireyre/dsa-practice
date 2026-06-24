# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        def f(root):
            if not root: return 0
            L,R = f(root.left),f(root.right)
            nonlocal res; res = max(res, L+R)
            return 1 + max(L,R)
        f(root)
        return res