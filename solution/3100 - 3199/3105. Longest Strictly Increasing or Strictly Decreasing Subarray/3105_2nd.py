# 3105. Longest Strictly Increasing or Strictly Decreasing Subarray | Easy
# https://leetcode.com/problems/longest-strictly-increasing-or-strictly-decreasing-subarray/
# Iterative, Single Pass
# 2nd attempt (12/11/2026) | 1st: 03/02/2025
# Complexity:
# + Time: O(n)
# + Space: O(1)

class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        if not nums:
            return 0

        ans = 1
        inc = 1
        dec = 1

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                inc += 1
                dec = 1
            elif nums[i] < nums[i - 1]:
                dec += 1
                inc = 1
            else:
                inc = 1
                dec = 1

            if inc > ans:
                ans = inc
            if dec > ans:
                ans = dec

        return ans
