# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = defaultdict(list)
        def f(root,H):
            if not root: return
            res[H].append(root.val)
            f(root.left,H+1); f(root.right, H+1)
        f(root,0)
        return list(res.values())