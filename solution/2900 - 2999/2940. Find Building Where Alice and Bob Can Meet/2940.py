# 2940. Find Building Where Alice and Bob Can Meet

# Binary Indexed Tree, Sorting, Binary Search
# Runtime: 84ms    

# Complexity:
# + Time: O((n + m) log(n) + n + m log(m))
# + Space: O(n + m)

import bisect
from typing import List


class BinaryIndexedTree:
    def __init__(self, n: int):
        self.inf = 1 << 30
        self.n = n
        self.c = [self.inf] * (n + 1)

    def update(self, x: int, v: int) -> None:
        while x <= self.n:
            self.c[x] = min(self.c[x], v)
            x += x & -x

    def query(self, x: int) -> int:
        mi = self.inf
        while x > 0:
            mi = min(mi, self.c[x])
            x -= x & -x
        return -1 if mi == self.inf else mi


class Solution:
    def leftmostBuildingQueries(
        self, heights: List[int], queries: List[List[int]]
    ) -> List[int]:
        n = len(heights)
        m = len(queries)

        for i in range(m):
            if queries[i][0] > queries[i][1]:
                queries[i] = [queries[i][1], queries[i][0]]

        idx = list(range(m))
        idx.sort(key=lambda i: -queries[i][1])

        s = sorted(heights)
        ans = [-1] * m
        j = n - 1
        tree = BinaryIndexedTree(n)

        for i in idx:
            l, r = queries[i]
            while j > r:
                # Rank of heights[j] in descending order (1-indexed)
                k = n - bisect.bisect_left(s, heights[j])
                tree.update(k, j)
                j -= 1

            if l == r or heights[l] < heights[r]:
                ans[i] = r
            else:
                k = n - bisect.bisect_right(s, heights[l])
                ans[i] = tree.query(k)

        return ans
