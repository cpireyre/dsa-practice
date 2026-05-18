import numpy as np
class Solution:
    def countSubstrings(self, s: str) -> int:
        N = len(s)
        dp = np.zeros((N,N), dtype=bool)
        for r in reversed(range(N)):
            for l in range(r,N):
                if s[l]==s[r] and (l-r<2 or dp[l-1][r+1]): dp[l][r] = True
        return int(sum(dp.flatten()))