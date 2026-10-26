# 2342. Max Sum of a Pair With Equal Sum of Digits
# Difficulty: Medium
# Link: https://leetcode.com/problems/max-sum-of-a-pair-with-equal-sum-of-digits/

# Hash Map
# Runtime: 37ms (13/02/2025 | 10pm - GMT+7)

# Complexity Analysis
# + Time: O(n * log10(max(nums)))
# + Space: O(n)

from typing import List


class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        digit_max = {}
        max_pair = -1

        for num in nums:
            # Compute digit sum
            n = num
            d_sum = 0
            while n > 0:
                d_sum += n % 10
                n //= 10

            if d_sum in digit_max:
                max_pair = max(max_pair, digit_max[d_sum] + num)
                digit_max[d_sum] = max(digit_max[d_sum], num)
            else:
                digit_max[d_sum] = num

        return max_pair
