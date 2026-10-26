# 3151. Special Array I
# Difficulty: Easy

# Iterative Approach
# Runtime: 0ms (03/02/2025 | 4pm - GMT+7)

# Complexity:
# + Time: O(n)
# + Space: O(1)

from typing import List


class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        for i in range(len(nums) - 1):
            if nums[i] % 2 == nums[i + 1] % 2:
                return False
        return True
