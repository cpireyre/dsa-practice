# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def f(root,m,M):
            if not root: return True
            if not m < root.val < M: return False
            return f(root.left,m,root.val) and f(root.right,root.val,M)
        return f(root,-1001,1001)