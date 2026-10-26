# 1368. Minimum Cost to Make at Least One Valid Path in a Grid
# Difficulty: Hard

# BFS (0-1)
# Runtime: 15ms (18/01/2025 | 11pm - GMT+7)

# Complexity:
# + Time: O(m * n)
# + Space: O(m * n)

from collections import deque
from typing import List


class Solution:
    DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def minCost(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dq = deque([(0, 0, 0)])  # (x, y, cost)
        visited = [[False] * n for _ in range(m)]

        while dq:
            x, y, cost = dq.popleft()
            if x == m - 1 and y == n - 1:
                return cost
            if visited[x][y]:
                continue
            visited[x][y] = True

            for d, (dx, dy) in enumerate(self.DIRECTIONS):
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    if grid[x][y] == d + 1:
                        dq.appendleft((nx, ny, cost))  # No cost
                    else:
                        dq.append((nx, ny, cost + 1))  # Cost 1

        return -1
