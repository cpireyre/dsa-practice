class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        xs = set(nums)
        res = 0
        for x in xs:
            if x - 1 in xs: continue
            length = 1
            while x + length in xs: length += 1
            res = max(res, length)
        return res