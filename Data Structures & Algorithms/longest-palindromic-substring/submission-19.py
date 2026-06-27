class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        L,R = 0,0
        for l in reversed(range(n)):
            for r in range(l,n):
                if s[l]==s[r] and (r-l<=2 or dp[l+1][r-1]):
                    dp[l][r] = True
                    if R-L < r-l: L,R = l,r
        return s[L:R+1]