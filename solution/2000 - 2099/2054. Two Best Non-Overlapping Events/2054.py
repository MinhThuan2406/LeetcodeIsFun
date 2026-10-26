# 2054. Two Best Non-Overlapping Events

# Binary Search, Recursion / DP
# Runtime: 59ms

# Complexity:
# + Time: O(n log(n))
# + Space: O(n)

import bisect
from typing import List


class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort(key=lambda x: x[0])
        n = len(events)
        starts = [e[0] for e in events]
        memo = {}

        def find_events(idx: int, cnt: int) -> int:
            if cnt == 2 or idx >= n:
                return 0
            state = (idx, cnt)
            if state in memo:
                return memo[state]

            end = events[idx][1]
            next_idx = bisect.bisect_right(starts, end)

            include = events[idx][2] + find_events(next_idx, cnt + 1)
            exclude = find_events(idx + 1, cnt)

            memo[state] = max(include, exclude)
            return memo[state]

        return find_events(0, 0)
