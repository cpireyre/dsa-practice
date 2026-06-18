class Solution:
    def numDecodings(self, s: str) -> int:
        N = len(s)
        dp = [0] * N + [1]
        for i in reversed(range(N)):
            dp[i] += dp[i+1] * (s[i] != '0')
            if i + 1 == N: continue
            dp[i] += dp[i+2]*(s[i]=='1' or (s[i]=='2' and s[i+1] in "0123456"))
        return dp[0]