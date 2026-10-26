# 2064. Minimized Maximum of Products Distributed to Any Store

# Binary Search
# Runtime: 22ms

# Complexity:
# + Time: O(m * log(max_quantity))
# + Space: O(1)

from typing import List


class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        def can_distribute(x: int) -> bool:
            stores_needed = sum((q + x - 1) // x for q in quantities)
            return stores_needed <= n

        left, right = 1, max(quantities)
        while left < right:
            mid = left + (right - left) // 2
            if can_distribute(mid):
                right = mid
            else:
                left = mid + 1

        return left
