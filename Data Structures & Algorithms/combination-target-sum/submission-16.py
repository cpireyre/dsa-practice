class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        def f(xs, l, total):
            if total == target:
                res.append(xs[:])
                return
            for r in range(l, len(nums)):
                if total + nums[r] > target: return
                xs.append(nums[r])
                f(xs, r, total + nums[r])
                xs.pop()
        f([],0,0)
        return res