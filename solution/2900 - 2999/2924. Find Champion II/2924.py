# 2924. Find Champion II

# In-Degree Analysis
# Runtime: 1ms

# Complexity:
# + Time: O(n + m), where m is the number of edges and n is the number of nodes
# + Space: O(n)

from typing import List


class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        in_degree = [0] * n
        for _, v in edges:
            in_degree[v] += 1

        champion = -1
        for i in range(n):
            if in_degree[i] == 0:
                if champion != -1:
                    return -1
                champion = i

        return champion
