class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r = 0,len(heights)-1
        res = 0
        while l < r:
            H = min(heights[l],heights[r])
            W = r - l
            res = max(res, H*W)
            if heights[l] < heights[r]: l += 1
            else: r -= 1
        return res