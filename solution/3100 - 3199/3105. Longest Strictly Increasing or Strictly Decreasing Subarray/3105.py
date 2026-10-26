# 3105. Longest Strictly Increasing or Strictly Decreasing Subarray
# Difficulty: Easy

# DP Arrays / Single Pass
# Runtime: 0ms (03/02/2025 | 4pm - GMT+7)

# Complexity:
# + Time: O(n)
# + Space: O(1)

from typing import List


class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return n

        inc = dec = 1
        max_len = 1

        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                inc += 1
            else:
                inc = 1

            if nums[i] < nums[i - 1]:
                dec += 1
            else:
                dec = 1

            max_len = max(max_len, inc, dec)

        return max_len
