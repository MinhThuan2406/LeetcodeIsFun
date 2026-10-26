# 1639. Number of Ways to Form a Target String Given a Dictionary

# 2D Array
# Dynamic Programming
# Runtime: 37ms (31/12/2024)

# Complexity:
# + Time: O(k * n + m * n)
# + Space: O(m * n)

from typing import List


class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        m, n = len(target), len(words[0])
        MOD = 10**9 + 7

        cnt = [[0] * 26 for _ in range(n)]
        for w in words:
            for j in range(n):
                cnt[j][ord(w[j]) - ord("a")] += 1

        f = [[0] * (n + 1) for _ in range(m + 1)]
        for j in range(n + 1):
            f[0][j] = 1

        for i in range(1, m + 1):
            t_idx = ord(target[i - 1]) - ord("a")
            for j in range(1, n + 1):
                f[i][j] = (f[i][j - 1] + f[i - 1][j - 1] * cnt[j - 1][t_idx]) % MOD

        return f[m][n]
