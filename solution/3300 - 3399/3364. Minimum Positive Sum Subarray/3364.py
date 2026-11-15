# 3364. Minimum Positive Sum Subarray | Easy
# https://leetcode.com/problems/minimum-positive-sum-subarray/
# Methods (keyword): Prefix Sum, Sliding Window
# Complexity:
# + Time: O(n^2)
# + Space: O(n)

class Solution:
    def minimumSumSubarray(self, nums: list[int], l: int, r: int) -> int:
        n = len(nums)
        min_pos_sum = float('inf')

        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        for k in range(l, r + 1):
            for i in range(n - k + 1):
                current_sum = prefix[i + k] - prefix[i]

                if current_sum > 0:
                    if current_sum < min_pos_sum:
                        min_pos_sum = current_sum

        return int(min_pos_sum) if min_pos_sum != float('inf') else -1
