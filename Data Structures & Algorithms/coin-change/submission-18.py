from math import inf
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [inf] * (amount+1)
        dp[0] = 0
        for c in coins:
            for a in range(amount+1):
                if a - c >= 0:
                    dp[a] = min(dp[a], dp[a-c] + 1)
        return dp[amount] if dp[amount] < inf else -1