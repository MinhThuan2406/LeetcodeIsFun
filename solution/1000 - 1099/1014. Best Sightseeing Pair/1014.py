# 1014. Best Sightseeing Pair

# Enumeration
# Runtime: 4ms

# Complexity:
# + Time: O(n)
# + Space: O(1)

from typing import List


class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        ans = 0
        mx = 0
        for j in range(len(values)):
            ans = max(ans, mx + values[j] - j)
            mx = max(mx, values[j] + j)

        return ans
