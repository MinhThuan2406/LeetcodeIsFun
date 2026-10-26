# 1448. Count Good Nodes in Binary Tree | Medium
# https://leetcode.com/problems/count-good-nodes-in-binary-tree/

# Tree Traversal
# Runtime: 116ms (26/10/2026 | 3pm - GMT+7)

# Complexity:
# + Time: O(N)
# + Space: O(H)


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node: TreeNode, max_val: int) -> int:
            if not node:
                return 0

            is_good = 1 if node.val >= max_val else 0
            current_max = max(max_val, node.val)

            left_count = dfs(node.left, current_max)
            right_count = dfs(node.right, current_max)

            return is_good + left_count + right_count

        return dfs(root, root.val)
