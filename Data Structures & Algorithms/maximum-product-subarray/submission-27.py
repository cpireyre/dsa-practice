class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = M = m = nums[0]
        for n in nums[1:]:
            extend = M * n
            M = max(extend, m * n, n)
            m = min(extend, m * n, n)
            res = max(res, M)
        return res