class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        m = M = res = nums[0]
        for n in nums[1:]:
            extend = M * n
            M = max(extend, n, m * n)
            m = min(extend, n, m * n)
            res = max(res, M)
        return res