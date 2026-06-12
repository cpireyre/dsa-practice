# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def f(root):
            if not root: return 0
            L,R = 1+f(root.left),1+f(root.right)
            return max(L,R)
        return f(root)