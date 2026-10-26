# 2593. Find Score of an Array After Marking All Elements

# Priority Queue (Min Heap)
# Runtime: 184ms

# Complexity:
# + Time: O(n * log(n))
# + Space: O(n)

import heapq
from typing import List


class Solution:
    def findScore(self, nums: List[int]) -> int:
        n = len(nums)
        vis = [False] * n
        pq = [(val, i) for i, val in enumerate(nums)]
        heapq.heapify(pq)

        ans = 0
        while pq:
            val, i = heapq.heappop(pq)
            if vis[i]:
                continue
            ans += val
            vis[i] = True
            if i > 0:
                vis[i - 1] = True
            if i + 1 < n:
                vis[i + 1] = True

        return ans
