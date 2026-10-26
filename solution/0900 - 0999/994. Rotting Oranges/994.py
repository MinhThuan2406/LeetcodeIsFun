# 994. Rotting Oranges | Medium
# https://leetcode.com/problems/rotting-oranges/

# Breadth-First Search
# Runtime: 3ms (26/10/2026 | 4pm - GMT+7)

# Complexity:
# + Time: O(mn)
# + Space: O(mn)

class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        queue = deque()
        fresh_count = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh_count += 1

        if fresh_count == 0:
            return 0

        minutes_elapsed = 0
        directions = ((-1, 0), (1, 0), (0, -1), (0, 1))

        while queue and fresh_count > 0:
            for _ in range (len(queue)):
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh_count -= 1
                        queue.append((nr, nc))
            minutes_elapsed += 1

        return minutes_elapsed if fresh_count == 0 else -1
