# 1267. Count Servers that Communicate
# Difficulty: Medium

# Count Row and Column Frequencies
# Runtime: 2ms (23/01/2025 | 10pm - GMT+7)

# Complexity:
# + Time: O(m * n)
# + Space: O(m + n)

from typing import List


class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        row_count = [0] * m
        col_count = [0] * n

        # First pass: Count servers in each row and column
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    row_count[i] += 1
                    col_count[j] += 1

        count = 0

        # Second pass: Check if each server can communicate
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (row_count[i] > 1 or col_count[j] > 1):
                    count += 1

        return count
