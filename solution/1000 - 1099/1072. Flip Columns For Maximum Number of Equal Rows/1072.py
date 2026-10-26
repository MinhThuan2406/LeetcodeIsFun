# 1072. Flip Columns For Maximum Number of Equal Rows

# Matrix, Pattern Matching, Hash Map
# Runtime: 31ms

# Complexity
# + Time: O(m * n)
# + Space: O(m * n)

from collections import defaultdict
from typing import List


class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        patterns = defaultdict(int)

        for row in matrix:
            first_bit = row[0]
            # Normalize pattern relative to the first element
            pattern = tuple(val ^ first_bit for val in row)
            patterns[pattern] += 1

        return max(patterns.values(), default=0)
