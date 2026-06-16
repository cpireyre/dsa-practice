class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1,max(piles)
        res = r
        while l <= r:
            m = l + (r-l)//2
            t = sum(math.ceil(float(p) / m) for p in piles)
            if t <= h:
                r = m - 1
                res = m
            else: l = m + 1
        return res