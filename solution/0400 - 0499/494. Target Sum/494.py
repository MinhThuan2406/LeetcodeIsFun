# 494. Target Sum

# Dynamic Programming, Recursion
# Runtime: 2ms

# Complexity:
# + Time: O(n * target)
# + Space: O(target)

from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total_sum = sum(nums)

        # If target + sum is odd or target is not reachable
        if (target + total_sum) % 2 != 0 or target > total_sum or target < -total_sum:
            return 0

        subset_sum = (target + total_sum) // 2
        return self._count_subsets(nums, subset_sum)

    def _count_subsets(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1  # Base case: 1 way to make sum 0

        for num in nums:
            for j in range(target, num - 1, -1):
                dp[j] += dp[j - num]

        return dp[target]
