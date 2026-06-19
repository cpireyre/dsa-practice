class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res =[]
        def f(xs,l):
            res.append(xs[:])
            for r in range(l,len(nums)):
                if r>l and nums[r]==nums[r-1]: continue
                xs.append(nums[r])
                f(xs,r+1)
                xs.pop()
        f([],0)
        return res