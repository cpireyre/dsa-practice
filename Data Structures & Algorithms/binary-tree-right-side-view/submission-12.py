# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def f(root,H):
            if not root: return
            nonlocal res
            if len(res) <= H: res.append(root.val)
            f(root.right, H+1)
            f(root.left, H+1)
        f(root,0)
        return res