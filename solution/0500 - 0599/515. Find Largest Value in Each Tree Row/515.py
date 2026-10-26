# 515. Find Largest Value in Each Tree Row

# BFS
# Runtime: 2ms

# Complexity:
# + Time: O(n)
# + Space: O(n)

from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        if not root:
            return ans

        q = deque([root])
        while q:
            t = float("-inf")
            for _ in range(len(q)):
                node = q.popleft()
                t = max(t, node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans.append(t)

        return ans
