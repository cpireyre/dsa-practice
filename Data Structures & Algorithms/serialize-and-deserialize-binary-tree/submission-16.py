# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []
        def f(root):
            if not root:
                res.append('n')
                return
            res.append(str(root.val))
            f(root.left); f(root.right)
        f(root)
        return " ".join(res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        xs = iter(data.split(" "))
        def f():
            x = next(xs)
            if x == 'n': return None
            root = TreeNode(int(x))
            root.left,root.right = f(),f()
            return root
        return f()