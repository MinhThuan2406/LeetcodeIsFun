# 2698. Find the Punishment Number of an Integer
# Difficulty: Medium
# Link: https://leetcode.com/problems/find-the-punishment-number-of-an-integer/

# Backtracking / Recursion
# Runtime: 24ms (15/02/2025 | 10pm - GMT+7)

# Complexity:
# + Time: O(n * log(n))
# + Space: O(1)


class Solution:
    def punishmentNumber(self, n: int) -> int:
        def can_partition(s: str, target: int, index: int) -> bool:
            if index == len(s):
                return target == 0
            if target < 0:
                return False

            num = 0
            for i in range(index, len(s)):
                num = num * 10 + int(s[i])
                if num > target:
                    break
                if can_partition(s, target - num, i + 1):
                    return True
            return False

        total = 0
        for i in range(1, n + 1):
            sq_str = str(i * i)
            if can_partition(sq_str, i, 0):
                total += i * i

        return total
