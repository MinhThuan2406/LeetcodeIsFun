# 2872. Maximum Number of K-Divisible Components

# Graph, DFS
# Graph Construction & DFS Traversal
# Runtime: 21ms

# Complexity:
# + Time: O(n)
# + Space: O(n)

from typing import List


class Solution:
    def maxKDivisibleComponents(
        self, n: int, edges: List[List[int]], values: List[int], k: int
    ) -> int:
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        ans = 0

        def dfs(u: int, prev: int) -> int:
            nonlocal ans
            tree_sum = values[u]
            for v in graph[u]:
                if v != prev:
                    tree_sum += dfs(v, u)

            if tree_sum % k == 0:
                ans += 1
            return tree_sum

        dfs(0, -1)
        return ans
