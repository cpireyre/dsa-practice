class Solution:
    def countSubstrings(self, s: str) -> int:
        N = len(s)
        res = 0
        dp = [[False] * N for _ in range(N)]
        for l in reversed(range(N)):
            for r in range(l,N):
                if s[l] == s[r] and (r - l <= 2 or dp[l+1][r-1]):
                    dp[l][r] = True
                    res += 1
        return res