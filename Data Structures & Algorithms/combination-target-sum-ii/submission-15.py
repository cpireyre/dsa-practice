class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        def f(xs,l,total):
            if total == target:
                res.append(xs[:])
                return
            for r in range(l, len(candidates)):
                if r > l and candidates[r] == candidates[r-1]: continue
                if total + candidates[r] > target: return
                xs.append(candidates[r])
                f(xs,r+1,total + candidates[r])
                xs.pop()
        f([],0,0)
        return res