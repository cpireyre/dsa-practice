class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        C = Counter(nums)
        F = [[] for _ in range(len(nums)+1)]
        for n,f in C.items(): F[f].append(n)
        res = []
        for ys in reversed(F):
            for n in ys:
                res.append(n)
                if len(res) == k: return res