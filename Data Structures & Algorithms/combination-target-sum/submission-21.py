class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort(); res = []
        def f(xs=[],l=0,total=0):
            if total == target:
                res.append(xs[:])
                return
            for r in range(l,len(nums)):
                if total + nums[r] > target: return
                if r>l and nums[r]==nums[r-1]: continue
                xs.append(nums[r]); f(xs,r,total+nums[r]); xs.pop()
        f()
        return res