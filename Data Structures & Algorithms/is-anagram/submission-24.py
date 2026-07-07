class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        S,T = [0]*26,[0]*26
        al = lambda c: ord(c) - ord('a')
        for c in s: S[al(c)] += 1
        for c in t: T[al(c)] += 1
        return all(S[i] == T[i] for i in range(26))