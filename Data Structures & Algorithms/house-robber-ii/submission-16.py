class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2: return nums[0] if nums else 0
        def rob2(nums):
            if len(nums) < 2: return nums[0] if nums else 0
            money = [0] * len(nums)
            money[0] = nums[0]; money[1] = max(nums[0],nums[1])
            for i in range(2, len(nums)):
                money[i] = max(money[i-1],money[i-2] + nums[i])
            return money[-1]
        return max(rob2(nums[1:]), rob2(nums[:-1]))