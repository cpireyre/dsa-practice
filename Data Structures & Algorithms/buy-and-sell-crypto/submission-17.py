from math import inf
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minBuy, maxP = inf, -inf
        for p in prices:
            minBuy = min(minBuy, p)
            maxP = max(maxP, p - minBuy)
        return maxP