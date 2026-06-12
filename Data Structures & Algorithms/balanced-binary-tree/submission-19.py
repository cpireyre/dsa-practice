# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def f(root):
            if not root: return (True, 0)
            L,R = f(root.left), f(root.right)
            balanced = L[0] and R[0] and abs(L[1] - R[1]) <= 1
            return (balanced, 1 + max(L[1], R[1]))
        return f(root)[0]