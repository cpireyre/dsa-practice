import numpy as np
class Solution:
    def longestPalindrome(self, s: str) -> str:
        N = len(s)
        dp = np.zeros((N+1,N+1))
        L,R = 0,0
        for l in reversed(range(N)):
            for r in range(l,N):
                if s[l]==s[r] and (dp[l+1][r-1] or r-l<2):
                    dp[l][r] = True
                    if R-L < r-l: L,R = l,r
        return s[L:R+1]