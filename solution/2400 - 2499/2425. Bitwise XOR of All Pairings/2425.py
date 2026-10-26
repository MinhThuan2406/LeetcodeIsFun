# 2425. Bitwise XOR of All Pairings

# Mathematical XOR Operations
# Runtime: 1ms (dd/mm/yyyy GMT+7)

# Complexity:
# + Time: O(1)
# + Space: O(1)

from functools import reduce
from operator import xor
from typing import List


class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        xor1 = reduce(xor, nums1, 0)
        xor2 = reduce(xor, nums2, 0)
        ans = 0
        if len(nums2) % 2:
            ans ^= xor1
        if len(nums1) % 2:
            ans ^= xor2
        return ans
