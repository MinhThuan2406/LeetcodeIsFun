# 2070. Most Beautiful Item for Each Query

# Sorting, Prefix Maximums, Binary Search
# Runtime: 32ms

# Complexity:
# + Time: O(n log n + m log n)
# + Space: O(n)

import bisect
from typing import List


class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort(key=lambda x: (x[0], -x[1]))
        n = len(items)

        max_beauty = [0] * n
        max_beauty[0] = items[0][1]
        for i in range(1, n):
            max_beauty[i] = max(max_beauty[i - 1], items[i][1])

        prices = [item[0] for item in items]
        answer = []

        for q in queries:
            idx = bisect.bisect_right(prices, q) - 1
            if idx >= 0:
                answer.append(max_beauty[idx])
            else:
                answer.append(0)

        return answer
