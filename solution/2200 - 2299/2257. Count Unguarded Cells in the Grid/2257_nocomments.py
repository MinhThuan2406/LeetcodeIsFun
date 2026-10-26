# 2257. Count Unguarded Cells in the Grid

# 2D Grid Simulation
# Runtime: 25ms

# Complexity:
# + Time: O(m * n + k)
# + Space: O(m * n)

from typing import List


class Solution:
    def countUnguarded(
        self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]
    ) -> int:
        grid = [[0] * n for _ in range(m)]

        for r, c in guards:
            grid[r][c] = 1
        for r, c in walls:
            grid[r][c] = 2

        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        for r, c in guards:
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                while 0 <= nr < m and 0 <= nc < n and grid[nr][nc] not in (1, 2):
                    if grid[nr][nc] == 0:
                        grid[nr][nc] = 3
                    nr += dr
                    nc += dc

        return sum(grid[i][j] == 0 for i in range(m) for j in range(n))
