class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        S,T = [0]*26,[0]*26
        al = lambda c: ord(c) - ord('a')
        for i in range(len(s)):
            S[al(s[i])] += 1
            T[al(t[i])] += 1
        return all(S[i] == T[i] for i in range(26))