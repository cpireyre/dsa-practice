class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        xs = defaultdict(int)
        for i,n in enumerate(nums):
            if target - n in xs: return [xs[target - n], i]
            xs[n] = i