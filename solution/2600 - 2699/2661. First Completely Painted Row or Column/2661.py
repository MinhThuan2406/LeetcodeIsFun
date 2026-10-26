# 2661. First Completely Painted Row or Column
# Difficulty: Medium

# Hash Map, Array
# Runtime: 23ms (20/01/2025 | 9pm - GMT+7)

# Complexity:
# + Time: O(m * n)
# + Space: O(m * n)

from typing import List


class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        idx = {}
        for i in range(m):
            for j in range(n):
                idx[mat[i][j]] = (i, j)

        row = [0] * m
        col = [0] * n

        for k, val in enumerate(arr):
            i, j = idx[val]
            row[i] += 1
            col[j] += 1
            if row[i] == n or col[j] == m:
                return k

        return -1
