class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        res = [0] * 26
        al = lambda c: ord(c) - ord('a')
        for i in range(len(s)):
            res[al(s[i])] += 1
            res[al(t[i])] -= 1
        return all(not c for c in res)