# 3203. Find Minimum Diameter After Merging Two Trees

# BFS, Graph, Union-Find / Tree Diameter
# Runtime: 148ms

# Complexity:
# + Time: O(n)
# + Space: O(n)

from collections import deque
from typing import List


class Solution:
    def minimumDiameterAfterMerge(
        self, edges1: List[List[int]], edges2: List[List[int]]
    ) -> int:
        diameter1 = self._get_diameter(edges1)
        diameter2 = self._get_diameter(edges2)
        combined_diameter = (diameter1 + 1) // 2 + (diameter2 + 1) // 2 + 1
        return max(diameter1, diameter2, combined_diameter)

    def _get_diameter(self, edges: List[List[int]]) -> int:
        n = len(edges) + 1
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # BFS to find the farthest node from node 0
        def bfs(start: int):
            q = deque([start])
            visited = [False] * n
            visited[start] = True
            farthest = start
            dist = -1

            while q:
                dist += 1
                for _ in range(len(q)):
                    node = q.popleft()
                    farthest = node
                    for neighbor in graph[node]:
                        if not visited[neighbor]:
                            visited[neighbor] = True
                            q.append(neighbor)

            return farthest, dist

        farthest_from_root, _ = bfs(0)
        _, diameter = bfs(farthest_from_root)
        return diameter
