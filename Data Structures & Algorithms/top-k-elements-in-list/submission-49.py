class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        C = Counter(nums)
        F = [[] for _ in range(len(nums) + 1)]
        for n,f in C.items(): F[f].append(n)
        res = []
        for xs in reversed(F):
            for n in xs:
                res.append(n)
                if len(res) == k: return res