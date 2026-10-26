# 2415. Reverse Odd Levels of Binary Tree

# BFS, Array
# Iterative Level-Order Traversal
# Runtime: 7ms

# Complexity:
# + Time: O(n)
# + Space: O(n)

from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        q = deque([root])
        is_odd_level = False

        while q:
            size = len(q)
            level_nodes = []

            for _ in range(size):
                node = q.popleft()
                level_nodes.append(node)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            if is_odd_level:
                left, right = 0, len(level_nodes) - 1
                while left < right:
                    level_nodes[left].val, level_nodes[right].val = (
                        level_nodes[right].val,
                        level_nodes[left].val,
                    )
                    left += 1
                    right -= 1

            is_odd_level = not is_odd_level

        return root
