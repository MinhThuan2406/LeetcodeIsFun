# 1726. Tuple with Same Product
# Difficulty: Medium

# Hash Map, Map, Array, Two Pointers
# Runtime: 206ms (06/02/2025 | 9pm - GMT+7)

# Complexity:
# + Time: O(n^2)
# + Space: O(n^2)

from collections import defaultdict
from typing import List


class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        product_count = defaultdict(int)
        n = len(nums)

        # Phase 1: Build frequency map of products from all pairs.
        for i in range(n):
            for j in range(i + 1, n):
                prod = nums[i] * nums[j]
                product_count[prod] += 1

        # Phase 2: For each product count, compute valid tuples.
        result = 0
        for count in product_count.values():
            if count > 1:
                result += 8 * (count * (count - 1) // 2)

        return result
