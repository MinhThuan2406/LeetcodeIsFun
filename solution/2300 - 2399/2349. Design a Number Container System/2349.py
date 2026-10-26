# 2349. Design a Number Container System
# Difficulty: Medium
# Link: https://leetcode.com/problems/design-a-number-container-system/

# Hash Map + Min-Heap (Lazy Removal)
# Runtime: 79ms (08/02/2025 | 10pm - GMT+7)

# Complexity:
# + Time: O(log n) for find() and O(log n) for change()
# + Space: O(M) where M is total changes

from collections import defaultdict
import heapq


class NumberContainers:
    def __init__(self):
        self.index_to_num = {}
        self.num_to_heap = defaultdict(list)

    def change(self, index: int, number: int) -> None:
        self.index_to_num[index] = number
        heapq.heappush(self.num_to_heap[number], index)

    def find(self, number: int) -> int:
        heap = self.num_to_heap[number]
        while heap:
            idx = heap[0]
            if self.index_to_num.get(idx) == number:
                return idx
            heapq.heappop(heap)
        return -1


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)
