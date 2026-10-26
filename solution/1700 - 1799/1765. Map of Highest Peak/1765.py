# 1765. Map of Highest Peak
# Difficulty: Medium

# BFS
# Runtime: 45ms (22/01/2025 | 8pm - GMT+7)

# Complexity:
# + Time: O(m * n)
# + Space: O(m * n)

from collections import deque
from typing import List


class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m, n = len(isWater), len(isWater[0])
        height = [[-1] * n for _ in range(m)]
        dq = deque()

        # Step 1: Add all water cells to the queue and set their height to 0
        for i in range(m):
            for j in range(n):
                if isWater[i][j] == 1:
                    dq.append((i, j))
                    height[i][j] = 0

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # Step 2: Perform BFS to propagate heights
        while dq:
            x, y = dq.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and height[nx][ny] == -1:
                    height[nx][ny] = height[x][y] + 1
                    dq.append((nx, ny))

        return height
