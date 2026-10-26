# 827. Making A Large Island
# Difficulty: Hard

# DSAs
# Methods & Approaches
# Runtime: 73ms (03/02/2025 | 4pm - GMT+7)

# Complexity:
# + Time: O(n^2)
# + Space: O(n^2)

from typing import List


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        area_map = {}
        island_id = 2

        def dfs(i: int, j: int, id_val: int) -> int:
            if i < 0 or i >= n or j < 0 or j >= n or grid[i][j] != 1:
                return 0
            grid[i][j] = id_val
            area = 1
            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                area += dfs(i + di, j + dj, id_val)
            return area

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    area_map[island_id] = dfs(i, j, island_id)
                    island_id += 1

        if not area_map:
            return 1

        max_area = 0
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    potential_area = 1
                    seen = set()
                    for di, dj in dirs:
                        ni, nj = i + di, j + dj
                        if 0 <= ni < n and 0 <= nj < n:
                            cur_id = grid[ni][nj]
                            if cur_id > 1 and cur_id not in seen:
                                seen.add(cur_id)
                                potential_area += area_map[cur_id]
                    max_area = max(max_area, potential_area)

        return n * n if max_area == 0 else max_area
