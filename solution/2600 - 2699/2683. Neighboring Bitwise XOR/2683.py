# 2683. Neighboring Bitwise XOR

# XOR Operations
# Runtime: 2ms (17/01/2025 GMT+7)

# Complexity:
# + Time: O(n)
# + Space: O(1)

from functools import reduce
from operator import xor
from typing import List


class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        # Valid if XOR sum of all elements is 0
        return reduce(xor, derived, 0) == 0
