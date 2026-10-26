# 1475. Final Prices With a Special Discount in a Shop

# Deque (Stack)
# Monotonic Stack, Iteration
# Runtime: 3ms

# Complexity:
# + Time: O(n)
# + Space: O(n)

from typing import List


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        ans = prices[:]
        stack = []

        for j in range(len(prices)):
            while stack and prices[j] <= prices[stack[-1]]:
                ans[stack.pop()] -= prices[j]
            stack.append(j)

        return ans
