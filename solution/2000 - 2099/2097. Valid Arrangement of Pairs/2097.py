# 2097. Valid Arrangement of Pairs

# Hierholzer's Algorithm (Eulerian Path)
# Runtime: 169ms

# Complexity:
# + Time: O(n)
# + Space: O(n)

from collections import defaultdict, deque
from typing import List


class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        # Step 1: Build adjacency list and degree maps
        graph = defaultdict(deque)
        in_degree = defaultdict(int)
        out_degree = defaultdict(int)

        for start, end in pairs:
            graph[start].append(end)
            out_degree[start] += 1
            in_degree[end] += 1

        # Step 2: Find starting node
        start_node = pairs[0][0]
        for node in graph:
            if out_degree[node] - in_degree[node] == 1:
                start_node = node
                break

        # Step 3: Hierholzer's algorithm
        result = []
        stack = [start_node]

        while stack:
            node = stack[-1]
            if graph[node]:
                stack.append(graph[node].pop())
            else:
                curr = stack.pop()
                if stack:
                    result.append([stack[-1], curr])

        result.reverse()
        return result
