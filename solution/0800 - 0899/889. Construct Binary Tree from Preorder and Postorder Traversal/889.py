# 889. Construct Binary Tree from Preorder and Postorder Traversal | Medium
# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/

# Hash Map | Recursion
# Runtime: 1ms (23/02/2025 | 9pm - GMT+7)

# Complexity:
# + Time: O(n)
# + Space: O(n)

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def constructFromPrePost(
        self, preorder: List[int], postorder: List[int]
    ) -> Optional[TreeNode]:
        post_map = {val: i for i, val in enumerate(postorder)}

        def build(pre_start: int, post_start: int, size: int) -> Optional[TreeNode]:
            if size == 0:
                return None
            root = TreeNode(preorder[pre_start])
            if size == 1:
                return root

            left_root = preorder[pre_start + 1]
            left_size = post_map[left_root] - post_start + 1
            right_size = size - 1 - left_size

            root.left = build(pre_start + 1, post_start, left_size)
            root.right = build(pre_start + 1 + left_size, post_start + left_size, right_size)
            return root

        return build(0, 0, len(preorder))
