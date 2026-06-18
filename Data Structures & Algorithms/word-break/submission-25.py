class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        N = len(s)
        dp = [False] * N + [True]
        for i in reversed(range(N+1)):
            for w in wordDict:
                L = len(w)
                if s[i:i+L] == w: dp[i] = dp[i+L]
                if dp[i]: break
        return dp[0]