# 3789. Minimum Cost to Acquire Required Items | Medium
# https://leetcode.com/problems/minimum-cost-to-acquire-required-items/
# Math, Greedy, Brute Force, Enumeration
# Complexity:
# + Time: O(1)
# + Space: O(1)

class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        def f(k):
            return k * costBoth + max(0, need1 - k) * cost1 + max(0, need2 - k) * cost2

        lo, hi = min(need1, need2), max(need1, need2)
        return min(f(0), f(lo), f(hi))
