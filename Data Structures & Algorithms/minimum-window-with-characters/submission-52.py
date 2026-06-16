class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t): return ""
        C = Counter(t)
        W = defaultdict(int)
        l = 0
        L,R = 0,len(s)
        have,need = 0,len(C)
        for r,c in enumerate(s):
            W[c] += 1
            have += c in C and W[c] == C[c]
            while have == need:
                if r - l < R - L: L,R = l,r
                W[s[l]] -= 1
                if s[l] in C and W[s[l]] < C[s[l]]: have -= 1
                l += 1
        return s[L:R+1] if R < len(s) else ""