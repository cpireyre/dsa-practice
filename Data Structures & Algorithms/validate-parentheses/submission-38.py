class Solution:
    def isValid(self, s: str) -> bool:
        M = {")":"(", "]":"[", "}":"{"}
        xs = []
        for c in s:
            if c in M:
                if not xs or M[c] != xs.pop(): return False
            else: xs.append(c)
        return not xs