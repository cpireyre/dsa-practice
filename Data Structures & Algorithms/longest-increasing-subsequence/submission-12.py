from bisect import bisect_left
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS = []
        for n in nums:
            if not LIS or n > LIS[-1]: LIS.append(n)
            else:
                i = bisect_left(LIS, n)
                LIS[i] = n
        return len(LIS)