class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def f(xs,l):
            res.append(xs[:])
            for r in range(l, len(nums)):
                xs.append(nums[r])
                f(xs,r+1)
                xs.pop()
        f([],0)
        return res