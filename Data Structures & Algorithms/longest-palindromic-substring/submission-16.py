import numpy as np
class Solution:
    def longestPalindrome(self, s: str) -> str:
        N = len(s)
        dp = np.zeros((N,N), dtype=bool)
        L,R = 0,0
        for l in reversed(range(N)):
            for r in range(l,N):
                if s[l] == s[r] and (r-l<2 or dp[l+1][r-1]):
                    dp[l][r] = True
                    if R - L < r - l: L,R = l,r
        return s[L:R+1]