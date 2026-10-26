# 3264. Final Array State After K Multiplication Operations I

# Simple Iteration / Min Heap
# Runtime: 1ms

# Complexity:
# + Time: O(n)
# + Space: O(1)

import heapq
from typing import List


class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        heap = [(val, i) for i, val in enumerate(nums)]
        heapq.heapify(heap)

        for _ in range(k):
            val, i = heapq.heappop(heap)
            new_val = val * multiplier
            nums[i] = new_val
            heapq.heappush(heap, (new_val, i))

        return nums
