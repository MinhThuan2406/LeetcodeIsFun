# 684. Redundant Connection
# Difficulty: Medium

# Disjoint Set Union
# Runtime: 0ms (29/01/2025 | 10pm - GMT+7)

# Complexity:
# + Time: O(n)
# + Space: O(n)

from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        p = list(range(n))

        def find(x: int) -> int:
            if p[x] != x:
                p[x] = find(p[x])
            return p[x]

        for u, v in edges:
            pa, pb = find(u - 1), find(v - 1)
            if pa == pb:
                return [u, v]
            p[pa] = pb
