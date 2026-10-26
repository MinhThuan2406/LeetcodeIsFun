# 2577. Minimum Time to Visit a Cell In a Grid

# Priority Queue (Dijkstra)
# Runtime: 129ms

# Complexity:
# + Time: O(m * n * log(m * n)) 
# + Space: O(m * n)

import heapq
from typing import List


class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        if grid[0][1] > 1 and grid[1][0] > 1:
            return -1

        m, n = len(grid), len(grid[0])
        dist = [[float("inf")] * n for _ in range(m)]
        dist[0][0] = 0

        pq = [(0, 0, 0)]  # (time, r, c)
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while pq:
            t, i, j = heapq.heappop(pq)
            if i == m - 1 and j == n - 1:
                return t
            if t > dist[i][j]:
                continue

            for di, dj in dirs:
                x, y = i + di, j + dj
                if 0 <= x < m and 0 <= y < n:
                    nt = t + 1
                    if nt < grid[x][y]:
                        nt = grid[x][y] + (grid[x][y] - nt) % 2
                    if nt < dist[x][y]:
                        dist[x][y] = nt
                        heapq.heappush(pq, (nt, x, y))

        return -1
