# 1980. Find Unique Binary String | Difficulty: Medium
# https://leetcode.com/problems/find-unique-binary-string/

# String | Diagonal Flipping
# Runtime: 0ms (20/02/2025 | 9pm - GMT+7)

# Complexity:
# + Time: O(n)
# + Space: O(n)

from typing import List


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        # Cantor's diagonal argument: flip i-th bit of i-th string
        return "".join("1" if nums[i][i] == "0" else "0" for i in range(len(nums)))
