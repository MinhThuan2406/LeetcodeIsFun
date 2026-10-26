# 802. Find Eventual Safe States
# Difficulty: Medium

# DFS
# Runtime: 5ms (24/01/2025 | 5pm - GMT+7)

# Complexity:
# + Time: O(V + E)
# + Space: O(V)

from typing import List


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        state = [0] * n  # 0: unvisited, 1: visiting, 2: safe

        def is_safe(node: int) -> bool:
            if state[node] > 0:
                return state[node] == 2
            state[node] = 1  # Mark as visiting
            for neighbor in graph[node]:
                if not is_safe(neighbor):
                    return False
            state[node] = 2  # Mark as safe
            return True

        return [i for i in range(n) if is_safe(i)]
