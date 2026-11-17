# 2911. Minimum Changes to Make K Semi-palindromes | Hard
# https://leetcode.com/problems/minimum-changes-to-make-k-semi-palindromes/
# Methods (keyword): Dynamic Programming, String Manipulation
# Complexity:
# + Time: O(n^3)
# + Space: O(n^2)

class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)

        divs = [[] for _ in range(n + 1)]
        for d in range(1, n):
            for length in range(2 * d, n + 1, d):
                divs[length].append(d)

        cost = [[0] * (n + 1) for _ in range(n + 1)]

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length
                sub = s[i:j]
                min_change = length

                for d in divs[length]:
                    current_d_change = 0
                    m = length // d
                    for g in range(d):
                        left = 0
                        right = m - 1
                        while left < right:
                            if sub[g + left * d] != sub[g + right * d]:
                                current_d_change += 1
                            left += 1
                            right -= 1
                    if current_d_change < min_change:
                        min_change = current_d_change
                cost[i][j] = min_change

        inf = float('inf')
        dp = [[inf] * (n + 1) for _ in range(k + 1)]
        dp[0][0] = 0

        for i in range(1, k + 1):
            for j in range(2 * i, n + 1):
                for p in range(2 * (i - 1), j - 1):
                    if dp[i-1][p] + cost[p][j] < dp[i][j]:
                        dp[i][j] = dp[i-1][p] + cost[p][j]

        return dp[k][n]
