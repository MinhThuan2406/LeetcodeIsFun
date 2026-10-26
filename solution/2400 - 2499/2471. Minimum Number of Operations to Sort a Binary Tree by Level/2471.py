# 2471. Minimum Number of Operations to Sort a Binary Tree by Level

# BFS, Queue, ArrayList, Map
# Runtime: 71ms

# Complexity:
# + Time: O(n log(k))
# + Space: O(n)

from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        queue = deque([root])
        total_operations = 0

        while queue:
            size = len(queue)
            level = []

            for _ in range(size):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            total_operations += self._calculate_minimum_swaps(level)

        return total_operations

    def _calculate_minimum_swaps(self, level: List[int]) -> int:
        n = len(level)
        sorted_indices = {val: idx for idx, val in enumerate(sorted(level))}
        arr = [sorted_indices[v] for v in level]

        visited = [False] * n
        swap_count = 0

        for i in range(n):
            if visited[i] or arr[i] == i:
                continue

            cycle_length = 0
            j = i
            while not visited[j]:
                visited[j] = True
                j = arr[j]
                cycle_length += 1

            swap_count += cycle_length - 1

        return swap_count
