# 2558. Take Gifts From the Richest Pile

# Max-Heap Priority Queue
# Runtime: 6ms

# Complexity:
# + Time: O(k * log(n) + n)
# + Space: O(n)

import heapq
import math
from typing import List


class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        max_heap = [-g for g in gifts]
        heapq.heapify(max_heap)

        for _ in range(k):
            largest = -heapq.heappop(max_heap)
            heapq.heappush(max_heap, -int(math.isqrt(largest)))

        return -sum(max_heap)
