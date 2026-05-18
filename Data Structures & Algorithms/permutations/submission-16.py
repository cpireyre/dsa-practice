class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def f(l):
            if l == len(nums):
                res.append(nums[:])
                return
            for r in range(l, len(nums)):
                nums[l],nums[r] = nums[r],nums[l]
                f(l+1)
                nums[l],nums[r] = nums[r],nums[l]
        f(0)
        return res