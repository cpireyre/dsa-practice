class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        xs = set(nums)
        res = 0
        for x in xs:
            if x - 1 not in xs:
                L = 0
                while x + L in xs: L += 1
                res = max(res, L)
        return res