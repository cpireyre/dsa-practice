class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []; candidates.sort()
        def f(xs,l,total):
            if total == target:
                res.append(xs[:])
                return
            for r in range(l,len(candidates)):
                if total + candidates[r] > target: return
                if r>l and candidates[r] == candidates[r-1]: continue
                f(xs + [candidates[r]],r+1,total+candidates[r])
        f([],0,0)
        return res