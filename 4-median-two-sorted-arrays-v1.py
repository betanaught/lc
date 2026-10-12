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

rand_len1 = random.randint(0, 1000)
rand_len2 = random.randint(0, 1000)
rand_nums1 = [random.randint(-10**6, 10**6) for i in range(rand_len1)]
rand_nums2 = [random.randint(-10**6, 10**6) for i in range(rand_len2)]

test_cases = {
    "case1": {
        "nums1": [1, 3],
        "nums2": [2]
        },
    "case2": {
        "nums1": [1, 2],
        "nums2": [3, 4]
        },
    "case_rand": {
        "nums1": rand_nums1,
        "nums2": rand_nums2
        }
    }

solution = Solution()
for key in test_cases:
    print(f"Testing case: {key}")
    nums1 = test_cases[key]["nums1"]
    nums2 = test_cases[key]["nums2"]
    print(f"nums1 values: {nums1}")
    print(f"nums2 values: {nums2}")
    output = solution.findMedianSortedArrays(nums1, nums2)
    print(output)
