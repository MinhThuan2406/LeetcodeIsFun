# 983. Minimum Cost For Tickets

# Memoization Array, Dynamic Programming, Recursive Traversal
# Runtime: 0ms

# Complexity:
# + Time: O(n)
# + Space: O(n)

from typing import List


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        memo = [-1] * len(days)

        def dfs(i: int) -> int:
            if i >= len(days):
                return 0
            if memo[i] != -1:
                return memo[i]

            one_day = costs[0] + dfs(i + 1)

            j = i
            while j < len(days) and days[j] < days[i] + 7:
                j += 1
            seven_days = costs[1] + dfs(j)

            j = i
            while j < len(days) and days[j] < days[i] + 30:
                j += 1
            thirty_days = costs[2] + dfs(j)

            memo[i] = min(one_day, seven_days, thirty_days)
            return memo[i]

        return dfs(0)
