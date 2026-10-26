# 2493. Divide Nodes Into the Maximum Number of Groups
# Difficulty: Hard

# Array, List, Queue (BFS)
# Bipartite Checking, Component Processing 
# Runtime: 343ms (03/02/2025 | 4pm - GMT+7)

# Complexity:
# + Time: O(m + n)
# + Space: O(m + n)

from collections import deque
from typing import List


class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u - 1].append(v - 1)
            g[v - 1].append(u - 1)

        global_visited = [False] * n
        total_groups = 0

        for i in range(n):
            if not global_visited[i]:
                groups = self._process_component(i, g, global_visited, n)
                if groups == -1:
                    return -1
                total_groups += groups

        return total_groups

    def _process_component(
        self, start: int, g: List[List[int]], global_visited: List[bool], n: int
    ) -> int:
        comp_nodes = [start]
        queue = deque([start])
        global_visited[start] = True

        while queue:
            cur = queue.popleft()
            for nei in g[cur]:
                if not global_visited[nei]:
                    global_visited[nei] = True
                    comp_nodes.append(nei)
                    queue.append(nei)

        max_groups = 0
        for node in comp_nodes:
            groups = self._bfs_groups(node, g, n)
            if groups == -1:
                return -1
            max_groups = max(max_groups, groups)

        return max_groups

    def _bfs_groups(self, start: int, g: List[List[int]], n: int) -> int:
        dist = [0] * n
        q = deque([start])
        dist[start] = 1
        mx = 1

        while q:
            cur = q.popleft()
            for nei in g[cur]:
                if dist[nei] == 0:
                    dist[nei] = dist[cur] + 1
                    mx = max(mx, dist[nei])
                    q.append(nei)
                elif abs(dist[nei] - dist[cur]) != 1:
                    return -1

        return mx
