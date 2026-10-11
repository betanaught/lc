class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        lookup = {}
        n = len(nums)

        for i in range(n):
            compliment = target - nums[i]
            if compliment in lookup:
                return [lookup[compliment], i]
            lookup[nums[i]] = i
        
        return []
        
