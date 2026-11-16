# 2243. Calculate Digit Sum of a String | Easy
# https://leetcode.com/problems/calculate-digit-sum-of-a-string/
# Methods (keyword): String Manipulation, Simulation
# Complexity:
# + Time: O(n)
# + Space: O(n)

class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            next_round = []

            for i in range (0, len(s), k):
                group = s[i : i + k]

                group_sum = sum(int(digit) for digit in group)

                next_round.append(str(group_sum))

            s = "".join(next_round)

        return s
