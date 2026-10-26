# 2466. Count Ways To Build Good Strings

# Dynamic Programming
# Runtime: 7ms

# Complexity:
# + Time: O(high)
# + Space: O(high)


class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        MOD = 10**9 + 7
        dp = [0] * (high + 1)
        dp[0] = 1
        count = 0

        for i in range(high + 1):
            if dp[i] > 0:
                if i + zero <= high:
                    dp[i + zero] = (dp[i + zero] + dp[i]) % MOD
                if i + one <= high:
                    dp[i + one] = (dp[i + one] + dp[i]) % MOD
            if i >= low:
                count = (count + dp[i]) % MOD

        return count
