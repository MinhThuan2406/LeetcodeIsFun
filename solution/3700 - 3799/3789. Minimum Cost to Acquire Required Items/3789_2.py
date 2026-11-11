# 3789. Minimum Cost to Acquire Required Items | Medium
# https://leetcode.com/problems/minimum-cost-to-acquire-required-items/
# Greedy
# Complexity:
# + Time: O(1)
# + Space: O(1)

class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        a = min(need1, need2)
        pair = min(cost1 + cost2, costBoth)
        if need1 >= need2:
            extra = min(cost1, costBoth)
        else:
            extra = min(cost2, costBoth)
        return a * pair + abs(need1 - need2) * extra
