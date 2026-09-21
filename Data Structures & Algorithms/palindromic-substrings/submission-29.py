class Solution:
    def countSubstrings(self, s: str) -> int:
        N = len(s)
        dp = [[False] * N for _ in range(N)]
        res = 0
        for l in reversed(range(N)):
            for r in range(l,N):
                if s[l]==s[r] and (r-l<=2 or dp[l+1][r-1]):
                    res += 1
                    dp[l][r] = True
        return res