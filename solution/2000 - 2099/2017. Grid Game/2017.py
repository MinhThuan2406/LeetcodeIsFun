# 2017. Grid Game
# Difficulty: Medium

# Greedy, Prefix Sum
# Runtime: 5ms (21/01/2025 | 10pm - GMT+7)

# Complexity:
# + Time: O(n)
# + Space: O(n)

from typing import List


class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        top_prefix = [0] * (n + 1)
        bottom_prefix = [0] * (n + 1)

        for j in range(1, n + 1):
            top_prefix[j] = top_prefix[j - 1] + grid[0][j - 1]
            bottom_prefix[j] = bottom_prefix[j - 1] + grid[1][j - 1]

        ans = float("inf")
        for j in range(n):
            s1 = top_prefix[n] - top_prefix[j + 1]  # Remaining top
            s2 = bottom_prefix[j]  # Covered bottom
            ans = min(ans, max(s1, s2))

        return ans
