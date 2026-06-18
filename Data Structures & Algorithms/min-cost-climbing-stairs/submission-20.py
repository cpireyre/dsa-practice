class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        for i in reversed(range(len(cost))):
            if i + 2 < len(cost): cost[i] += min(cost[i+1],cost[i+2])
        return min(cost[0],cost[1])