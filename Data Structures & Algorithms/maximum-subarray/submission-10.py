class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = best = nums[0]
        for n in nums[1:]:
            curr = max(n, curr + n)
            best = max(curr, best)
        return best