# 3243. Shortest Distance After Road Addition Queries I

# BFS 
# Runtime: 91ms

# Complexity:
# + Time: O(queries.length * (n + edges))
# + Space: O(n + edges)

from collections import deque
from typing import List


class Solution:
    def shortestDistanceAfterQueries(
        self, n: int, queries: List[List[int]]
    ) -> List[int]:
        graph = [[] for _ in range(n)]
        for i in range(n - 1):
            graph[i].append(i + 1)

        def bfs() -> int:
            queue = deque([(0, 0)])
            visited = [False] * n
            visited[0] = True

            while queue:
                node, dist = queue.popleft()
                if node == n - 1:
                    return dist

                for neighbor in graph[node]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        queue.append((neighbor, dist + 1))

            return -1

        result = []
        for u, v in queries:
            graph[u].append(v)
            result.append(bfs())

        return result
