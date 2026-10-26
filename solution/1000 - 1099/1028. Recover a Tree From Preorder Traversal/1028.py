# 1028. Recover a Tree From Preorder Traversal | Difficulty: Hard
# https://leetcode.com/problems/recover-a-tree-from-preorder-traversal/

# Stack | Iteration
# Runtime: 6ms (22/02/2025 | 11pm - GMT+7)

# Complexity:
# + Time: O(n) - n is the length of the traversal string
# + Space: O(n) - n is the length of the traversal string

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        stack = []
        i = 0
        n = len(traversal)

        while i < n:
            depth = 0
            while i < n and traversal[i] == "-":
                depth += 1
                i += 1

            val = 0
            while i < n and traversal[i] != "-":
                val = val * 10 + int(traversal[i])
                i += 1

            node = TreeNode(val)
            while len(stack) > depth:
                stack.pop()
            if stack:
                if stack[-1].left is None:
                    stack[-1].left = node
                else:
                    stack[-1].right = node
            stack.append(node)

        return stack[0] if stack else None
