# 1800. Maximum Ascending Subarray Sum
# Difficulty: Easy

# Single Pass
# Runtime: 0ms (04/02/2025 | 11am - GMT+7)

# Complexity:
# + Time: O(n)
# + Space: O(1)

from typing import List


class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        max_sum = 0
        current_sum = 0
        for i in range(len(nums)):
            if i == 0 or nums[i] > nums[i - 1]:
                current_sum += nums[i]
            else:
                max_sum = max(max_sum, current_sum)
                current_sum = nums[i]

        return max(max_sum, current_sum)
