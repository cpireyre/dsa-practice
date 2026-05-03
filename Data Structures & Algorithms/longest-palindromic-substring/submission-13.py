import numpy as np
class Solution:
    def longestPalindrome(self, s: str) -> str:
        N = len(s)
        L,R = 0,0
        dp = np.zeros((N+1,N+1), dtype=bool)
        for l in reversed(range(N)):
            for r in range(l,N):
                if s[l] == s[r] and (dp[l+1][r-1] or r-l<2):
                    dp[l][r] = True
                    if r - l > R - L : L,R = l,r
        return s[L:R+1]