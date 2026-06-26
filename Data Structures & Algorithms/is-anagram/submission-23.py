class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        A,B = [0] * 26,[0]*26
        al = lambda c: ord(c) - ord('a')
        for c in s: A[al(c)] += 1
        for c in t: B[al(c)] += 1
        return all(A[i] == B[i] for i in range(26))