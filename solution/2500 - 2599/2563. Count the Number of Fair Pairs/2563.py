# 2563. Count the Number of Fair Pairs

# Sorting and Two-Pointer / Binary Search
# Runtime: 62ms

import bisect
from typing import List


class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        count = 0
        n = len(nums)

        for i in range(n):
            left_target = lower - nums[i]
            right_target = upper - nums[i]

            j_start = bisect.bisect_left(nums, left_target, i + 1, n)
            j_end = bisect.bisect_right(nums, right_target, i + 1, n)

            count += j_end - j_start

        return count
