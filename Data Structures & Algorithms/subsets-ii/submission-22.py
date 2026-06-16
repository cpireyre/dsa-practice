class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        def f(l,xs):
            res.append(xs[:])
            for r in range(l,len(nums)):
                if r>l and nums[r] == nums[r-1]: continue
                xs.append(nums[r])
                f(r+1,xs)
                xs.pop()
        f(0,[])
        return res