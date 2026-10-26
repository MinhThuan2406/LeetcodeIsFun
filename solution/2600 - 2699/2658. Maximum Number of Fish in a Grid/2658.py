# 2658. Maximum Number of Fish in a Grid
# Difficulty: Medium

# BFS, Queue
# Runtime: 5ms (28/01/2025 | 7pm - GMT+7)

# Complexity:
# + Time: O(m * n)
# + Space: O(m * n)

from collections import deque
from typing import List


class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        max_fish = 0
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def bfs(i: int, j: int) -> int:
            fish_count = 0
            q = deque([(i, j)])

            while q:
                x, y = q.popleft()
                if grid[x][y] > 0:
                    fish_count += grid[x][y]
                    grid[x][y] = 0
                    for dx, dy in dirs:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] > 0:
                            q.append((nx, ny))

            return fish_count

        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0:
                    max_fish = max(max_fish, bfs(i, j))

        return max_fish
