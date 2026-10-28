# 25. Reverse Nodes in k-Group | Hard
# https://leetcode.com/problems/reverse-nodes-in-k-group/
# Linked List
# Complexity:
# + Time: O(N) where N is the number of nodes in the linked list.
# + Space: O(1) for using a constant amount of extra space.

# Solution 1
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None: # type: ignore
        dummy = ListNode(0) # type: ignore
        dummy.next = head
        prev_group_tail = dummy
        curr = head

        while curr:
            group_start = curr
            count = 0
            while count < k and curr:
                curr = curr.next
                count += 1
            if count < k:
                break

            prev = None
            temp_curr = group_start
            for _ in range(k):
                next_node = temp_curr.next
                temp_curr.next = prev
                prev = temp_curr
                temp_curr = next_node

            group_start.next = curr
            prev_group_tail.next = prev
            prev_group_tail = group_start

        return dummy.next
