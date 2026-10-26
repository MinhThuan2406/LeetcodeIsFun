# 1975. Maximum Matrix Sum

# Array, Matrix
# Runtime: 5ms

# Complexity:
# + Time: O(n^2)
# + Space: O(1)

from typing import List


class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        total_sum = 0
        negative_count = 0
        min_abs_value = float("inf")

        for row in matrix:
            for val in row:
                abs_val = abs(val)
                total_sum += abs_val
                if val < 0:
                    negative_count += 1
                if abs_val < min_abs_value:
                    min_abs_value = abs_val

        if negative_count & 1:
            total_sum -= 2 * min_abs_value

        return total_sum
