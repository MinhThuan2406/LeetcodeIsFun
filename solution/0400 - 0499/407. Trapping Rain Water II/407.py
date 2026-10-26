# 407. Trapping Rain Water II
# Difficulty: Hard

# Priority Queue (Min-Heap), BFS
# Runtime: 19ms (19/01/2025 | 10pm - GMT+7)

# Complexity:
# + Time: O(m * n * log(m * n))
# + Space: O(m * n)

import heapq
from typing import List


class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if not heightMap or not heightMap[0]:
            return 0

        m, n = len(heightMap), len(heightMap[0])
        vis = [[False] * n for _ in range(m)]
        pq = []

        for i in range(m):
            for j in range(n):
                if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                    heapq.heappush(pq, (heightMap[i][j], i, j))
                    vis[i][j] = True

        ans = 0
        dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        while pq:
            h, r, c = heapq.heappop(pq)
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and not vis[nr][nc]:
                    ans += max(0, h - heightMap[nr][nc])
                    vis[nr][nc] = True
                    heapq.heappush(pq, (max(h, heightMap[nr][nc]), nr, nc))

        return ans
