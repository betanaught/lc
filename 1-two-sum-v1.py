class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            js = [idx for idx in range(len(nums)) if idx != i]
            for j in js:
                if nums[i] + nums[j] == target:
                    return [i, j]

            return []
