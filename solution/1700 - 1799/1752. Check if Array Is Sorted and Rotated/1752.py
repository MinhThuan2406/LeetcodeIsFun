# 1752. Check if Array Is Sorted and Rotated
# Difficulty: Easy

# Single Pass
# Runtime: 0ms (03/02/2025 | 4pm - GMT+7)

# Complexity:
# + Time: O(n)
# + Space: O(1)

from typing import List


class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        count_drops = 0

        for i in range(n):
            if nums[i] > nums[(i + 1) % n]:
                count_drops += 1

        return count_drops <= 1
