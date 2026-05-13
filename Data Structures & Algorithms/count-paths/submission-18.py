import numpy as np
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = np.zeros((m+1,n+1))
        dp[m-1][n-1] = 1
        for i,j in product(reversed(range(m)),reversed(range(n))):
            dp[i][j] += dp[i+1][j] + dp[i][j+1]
        return int(dp[0][0])