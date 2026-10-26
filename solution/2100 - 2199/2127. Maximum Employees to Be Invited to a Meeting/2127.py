# 2127. Maximum Employees to Be Invited to a Meeting
# Difficulty: Hard

# Topological Sorting (BFS-based)
# Runtime: 35ms (26/01/2025 | 11pm - GMT+7)

# Complexity:
# + Time: O(n)
# + Space: O(n)

from collections import deque
from typing import List


class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        return max(self._max_cycle(favorite), self._topological_sort(favorite))

    def _max_cycle(self, fa: List[int]) -> int:
        n = len(fa)
        vis = [False] * n
        ans = 0

        for i in range(n):
            if vis[i]:
                continue
            cycle = []
            j = i
            while not vis[j]:
                cycle.append(j)
                vis[j] = True
                j = fa[j]

            for k in range(len(cycle)):
                if cycle[k] == j:
                    ans = max(ans, len(cycle) - k)

        return ans

    def _topological_sort(self, fa: List[int]) -> int:
        n = len(fa)
        indeg = [0] * n
        dist = [1] * n

        for v in fa:
            indeg[v] += 1

        q = deque([i for i in range(n) if indeg[i] == 0])

        while q:
            i = q.popleft()
            dist[fa[i]] = max(dist[fa[i]], dist[i] + 1)
            indeg[fa[i]] -= 1
            if indeg[fa[i]] == 0:
                q.append(fa[i])

        ans = 0
        for i in range(n):
            if i == fa[fa[i]]:
                ans += dist[i]

        return ans
