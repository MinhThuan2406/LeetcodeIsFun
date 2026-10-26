# 3066. Minimum Operations to Exceed Threshold Value II
# Difficulty: Medium
# Link: https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-ii/

# Priority Queue (Min-Heap)
# Runtime: 148ms (13/02/2025 | 11pm - GMT+7)

# Complexity Analysis
# + Time: O(n * log(n)) where n is the number of elements in the input array.
# + Space: O(n) where n is the number of elements in the input array.

import heapq
from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        ans = 0

        while len(nums) > 1 and nums[0] < k:
            x = heapq.heappop(nums)
            y = heapq.heappop(nums)
            heapq.heappush(nums, 2 * x + y)
            ans += 1

        return ans
