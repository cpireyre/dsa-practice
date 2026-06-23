# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        indices = {val:idx for idx,val in enumerate(inorder)}
        xs = iter(preorder)
        def f(l,r):
            if l > r: return
            x = next(xs)
            sep = indices[x]
            root = TreeNode(x)
            root.left,root.right = f(l,sep-1),f(sep+1,r)
            return root
        return f(0,len(preorder)-1)