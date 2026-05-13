class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        Max = Min = Best = nums[0]
        for n in nums[1:]:
            extend = Max * n
            Max = max(n, extend, Min * n)
            Min = min(n, extend, Min * n)
            Best = max(Best, Max)
        return Best