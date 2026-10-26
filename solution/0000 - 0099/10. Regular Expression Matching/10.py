# 10. Regular Expression Matching | Hard
# https://leetcode.com/problems/regular-expression-matching/

# Dynamic Programming
# Runtime: 6ms (26/10/2026 | 4pm - GMT+7)

# Complexity:
# + Time: O(mn)
# + Space: O(mn)

from functools import lru_cache

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        @lru_cache(None)

        def dfs(i: int, j: int) -> bool:
            if j == len(p):
                return i == len(s)

            first_match = i < len(s) and p[j] in {s[i], '.'}

            if j + 1 < len(p) and p[j + 1] == '*':
                return dfs(i, j + 2) or (first_match and dfs(i + 1, j))

            return first_match and dfs(i + 1, j + 1)

        return dfs(0, 0)
