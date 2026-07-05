class Solution:
    def isValid(self, s: str) -> bool:
        M = {
            ")":"(",
            "]":"[",
            "}":"{"
            }
        stack = []
        for c in s:
            if c in M:
                if not stack or stack.pop() != M[c]: return False
            else: stack.append(c)
        return not stack