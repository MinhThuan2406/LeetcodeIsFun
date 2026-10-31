# 3665. Twisted Mirror Path Count | Medium
# https://leetcode.com/problems/twisted-mirror-path-count/
# Dynamic Programming, 2D Prefix Sum
# Complexity:
# + Time: O(mn)
# + Space: O(mn)

class Solution:
    def uniquePaths(self, grid: list[list[int]]) -> int:
        M = len(grid)
        N = len(grid[0])
        MOD = 10**9 + 7

        after_r = [[None] * N for _ in range(M)]
        after_d = [[None] * N for _ in range(M)]

        for r in range(M - 1, -1, -1):
            for c in range(N - 1, -1, -1):
                if grid[r][c] == 0:
                    after_r[r][c] = (r, c, 1)
                else:
                    if r + 1 < M:
                        after_r[r][c] = after_d[r + 1][c]
                    else:
                        after_r[r][c] = None

                if grid[r][c] == 0:
                    after_d[r][c] = (r, c, 0)
                else:
                    if c + 1 < N:
                        after_d[r][c] = after_r[r][c + 1]
                    else:
                        after_d[r][c] = None

        dp = [[[0, 0] for _ in range(N)] for _ in range(M)]
        if grid[0][0] == 0:
            dp[0][0][0] = 1
        else:
            return 0

        for r in range(M):
            for c in range(N):
                ways = (dp[r][c][0] + dp[r][c][1]) % MOD
                if ways == 0 and not (r == 0 and c == 0):
                    continue
                if r == 0 and c == 0:
                    ways = 1

                if c + 1 < N:
                    dest = after_r[r][c + 1]
                    if dest:
                        dr, dc, dd = dest
                        dp[dr][dc][dd] = (dp[dr][dc][dd] + ways) % MOD

                if r + 1 < M:
                    dest = after_d[r + 1][c]
                    if dest:
                        dr, dc, dd = dest
                        dp[dr][dc][dd] = (dp[dr][dc][dd] + ways) % MOD

        return (dp[M - 1][N - 1][0] + dp[M - 1][N - 1][1]) % MOD
