# 2601. Prime Subtraction Operation

# Greedy, Sieve / Prime Testing
# Runtime: 9ms

# Complexity:
# + Time: O(n * sqrt(max_val))
# + Space: O(1)

import math
from typing import List


class Solution:
    def _is_prime(self, n: int) -> bool:
        if n <= 1:
            return False
        for i in range(2, int(math.isqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    def _find_largest_prime(self, n: int) -> int:
        for i in range(n - 1, 1, -1):
            if self._is_prime(i):
                return i
        return 0

    def primeSubOperation(self, nums: List[int]) -> bool:
        prev = 0

        for i in range(len(nums)):
            if nums[i] <= prev:
                return False

            max_subtract = nums[i] - prev - 1
            if max_subtract > 0:
                prime = self._find_largest_prime(max_subtract + 1)
                nums[i] -= prime

            prev = nums[i]

        return True
