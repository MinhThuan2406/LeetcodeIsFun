# 23. Merge k Sorted Lists | Hard
# https://leetcode.com/problems/merge-k-sorted-lists/

# Runtime: 9ms (27/10/2026 | 2pm - GMT+7)

# Complexity:
# + Time: O(k log n)
# + Space: O(k)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq

class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        heap = []

        for i, head in enumerate(lists):
            if head:
                heapq.heappush(heap, (head.val, i, head))

        dummy = ListNode(0)
        curr = dummy

        while heap:
            val, i, node = heapq.heappop(heap)

            curr.next = node
            curr = curr.next

            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))

        return dummy.next
