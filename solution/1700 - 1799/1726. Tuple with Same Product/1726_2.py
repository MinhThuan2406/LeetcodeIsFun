# 1726. Tuple with Same Product
# Difficulty: Medium

# Hash Map, Map, Array, Two Pointers
# Runtime: 170ms (06/02/2025 | 9pm - GMT+7)

# Complexity:
# + Time: O(n^2)
# + Space: O(n)

# 2nd Approach

from collections import defaultdict
from typing import List


class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        map_prod = defaultdict(int)
        n = len(nums)
        res = 0

        for i in range(n):
            for j in range(i + 1, n):
                prod = nums[i] * nums[j]
                res += 8 * map_prod[prod]
                map_prod[prod] += 1

        return res
