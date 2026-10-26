# 19. Remove Nth Node From End of List | Medium
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Two-Pointers
# Runtime: 0ms (26/10/2026 | 5pm - GMT+7)

# Complexity:
# + Time: O(n)
# + Space: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        dummy = ListNode(0, head)
        fast = dummy
        slow = dummy

        for _ in range(n + 1):
            fast = fast.next

        while fast is not None:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next
        return dummy.next
