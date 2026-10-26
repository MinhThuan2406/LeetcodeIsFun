# 2364. Count Number of Bad Pairs
# Difficulty: Medium

# Hash Map
# Counting
# Runtime: 39ms (09/02/2025 | 9pm - GMT+7)

# Complexity:
# + Time: O(n)
# + Space: O(n)

from collections import defaultdict
from typing import List


class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)
        total_pairs = n * (n - 1) // 2
        freq_count = defaultdict(int)

        for i, val in enumerate(nums):
            diff = val - i
            freq_count[diff] += 1

        good_pairs = sum(cnt * (cnt - 1) // 2 for cnt in freq_count.values())
        return total_pairs - good_pairs
