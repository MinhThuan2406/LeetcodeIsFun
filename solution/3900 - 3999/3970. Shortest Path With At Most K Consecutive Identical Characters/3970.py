# 3970. Shortest Path With At Most K Consecutive Identical Characters | Medium
# https://leetcode.com/problems/shortest-path-with-at-most-k-consecutive-identical-characters/
# Dijkstra, Priority Queue, 2D Array
# Complexity:
# + Time: O((n + m) log(n * k)), n = number of nodes, m = number of edges
# + Space: O(n * k)

from heapq import heappush, heappop

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int: # type: ignore
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))

        INF = float('inf')
        dist = [[INF] * (k + 1) for _ in range(n)]
        min_run = [k + 1] * n

        dist[0][1] = 0
        pq = [(0, 0, 1)]

        while pq:
            d, u, run = heappop(pq)

            if d > dist[u][run] or run >= min_run[u]:
                continue

            if u == n - 1:
                return d

            min_run[u] = run
            label_u = labels[u]

            for v, w in adj[u]:
                new_run = run + 1 if labels[v] == label_u else 1
                if new_run > k:
                    continue

                new_dist = d + w
                if new_dist < dist[v][new_run]:
                    dist[v][new_run] = new_dist
                    heappush(pq, (new_dist, v, new_run))

        return -1
