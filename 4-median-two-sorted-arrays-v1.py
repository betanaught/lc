import random

class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        nums = sorted(nums1 + nums2) # cowardly sort, be a man
        if len(nums) % 2 != 0: # if len is odd
            m = len(nums) // 2
            median = nums[m]
        else:                  # if len is even
            m1 = len(nums) // 2
            m2 = m1 - 1
            median = (nums[m1] + nums[m2]) / 2
        return median

len1 = random.randint(0, 1000)
len2 = random.randint(0, 1000)
nums1 = [random.randint(-10**6, 10**6) for i in range(len1)]
nums2 = [random.randint(-10**6, 10**6) for i in range(len1)]

solution = Solution()
output = solution.findMedianSortedArrays(nums1, nums2)
print(output)
