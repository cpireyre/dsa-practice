import numpy as np
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        M,N = len(text1),len(text2)
        dp = np.zeros((M+1,N+1))
        for i in reversed(range(M)):
            for j in reversed(range(N)):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]
                else: dp[i][j] = max(dp[i+1][j],dp[i][j+1])
        return int(dp[0][0])