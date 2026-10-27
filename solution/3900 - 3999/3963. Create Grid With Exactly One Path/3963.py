# 3963. Create Grid With Exactly One Path | Medium
# https://leetcode.com/problems/create-grid-with-exactly-one-path/

# BFS
# Runtime: 1ms (27/10/2026 | 9am - GMT+7)

# Complexity:
# + Time: O(m*n)
# + Space: O(m*n)

class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        grid = [["#"] * n for _ in range(m)]

        for col in range(n):
            grid[0][col] = "."

        for row in range(m):
            grid[row][n - 1] = "."

        return ["".join(row) for row in grid]
