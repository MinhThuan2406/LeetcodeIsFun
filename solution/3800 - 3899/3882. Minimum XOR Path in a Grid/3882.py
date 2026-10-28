# 3882. Minimum XOR Path in a Grid | Medium
# https://leetcode.com/problems/minimum-xor-path-in-a-grid/
# Dynamic Programming
# Complexity:
# + Time: O(N * M * K) where N is the number of rows, M is the number of columns, and K is the number of unique XOR values that can be generated along the paths.
# + Space: O(N * M * K) for storing the reachable XOR values at each cell in the grid.

# Solution 1
class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        reachable = [[set() for _ in range(cols)] for _ in range(rows)]
        reachable[0][0].add(grid[0][0])

        for r in range(rows):
            for c in range(cols):
                if r == 0 and c == 0:
                    continue

                previous_values = set()

                if r > 0:
                    previous_values |= reachable[r - 1][c]
                if c > 0:
                    previous_values |= reachable[r][c - 1]

                for value in previous_values:
                    reachable[r][c].add(value ^ grid[r][c])

        return min(reachable[rows - 1][cols - 1])

# Solution 2
# class Solution:
#     def minCost(self, grid: list[list[int]]) -> int:
#         m, n = len(grid), len(grid[0])
#         dp = [set() for _ in range(n)]

#         x = 0
#         for c in range(n):
#             x ^= grid[0][c]
#             dp[c].add(x)

#         for r in range(1, m):
#             dp[0] = {v ^ grid[r][0] for v in dp[0]}
#             for c in range(1, n):
#                 dp[c] = {v ^ grid[r][c] for v in dp[c] | dp[c - 1]}

#         return min(dp[n - 1])
