# 3693. Climbing Stairs II | Medium
# https://leetcode.com/problems/climbing-stairs-ii/
# Dynamic Programming
# Complexity:
# + Time: O(n)
# + Space: O(n)

class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        dp = [float('inf')] * (n + 1)

        dp[0] = 0

        for i in range(1, n + 1):
            step_cost = costs[i - 1]

            if i - 1 >= 0:
                dp[i] = min(dp[i], dp[i - 1] + step_cost + 1)

            if i - 2 >= 0:
                dp[i] = min(dp[i], dp[i - 2] + step_cost + 4)

            if i - 3 >= 0:
                dp[i] = min(dp[i], dp[i - 3] + step_cost + 9)

        return int(dp[n])
