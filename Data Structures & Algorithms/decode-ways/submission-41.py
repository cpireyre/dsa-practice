class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0] * len(s) + [1]
        for i in reversed(range(len(s))):
            dp[i] += dp[i+1] * (s[i]!='0')
            if i+1 == len(s): continue
            dp[i] += dp[i+2] * (s[i]=='1' or (s[i]=='2' and s[i+1] in "0123456"))
        return dp[0]