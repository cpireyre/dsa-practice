class Solution:
    def longestPalindrome(self, s: str) -> str:
        N = len(s)
        dp = [[False] * N for _ in range(N)]
        L,R = 0,0
        for i in reversed(range(N)):
            for j in range(i,N):
                if s[i] == s[j] and (j-i<=2 or dp[i+1][j-1]):
                    dp[i][j] = True
                    if j-i > R-L: L,R = i,j
        return s[L:R+1]