# 1792. Maximum Average Pass Ratio

# Priority Queue (Max-Heap)
# Greedy Approach
# Runtime: 329ms

# Complexity:
# + Time: O(n * log(n))
# + Space: O(n)

import heapq
from typing import List


class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        # Heap elements: (-gain, pass_count, total_count)
        def gain(p: int, t: int) -> float:
            return (p + 1) / (t + 1) - p / t

        max_heap = [(-gain(p, t), p, t) for p, t in classes]
        heapq.heapify(max_heap)

        for _ in range(extraStudents):
            cur_gain, p, t = heapq.heappop(max_heap)
            p += 1
            t += 1
            heapq.heappush(max_heap, (-gain(p, t), p, t))

        return sum(p / t for _, p, t in max_heap) / len(classes)
