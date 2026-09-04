from bisect import bisect_left
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = []
        for n in nums:
            if not dp or n > dp[-1]: dp.append(n)
            else:
                idx = bisect_left(dp, n)
                dp[idx] = n
        return len(dp)