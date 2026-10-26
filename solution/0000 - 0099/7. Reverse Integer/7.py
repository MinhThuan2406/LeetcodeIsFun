# 7. Reverse Integer | Medium
# https://leetcode.com/problems/reverse-integer/

# Math
# Runtime: 1ms (26/10/2026 | 3pm - GMT+7)

# Complexity:
# + Time: O(log|x|)
# + Space: O(1)


class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN, INT_MAX = -2**31, 2**31 - 1

        sign = -1 if x < 0 else 1
        x = abs(x)
        reversed_num = 0

        while x:
            digit = x % 10
            x //= 10

            if reversed_num > (INT_MAX - digit) // 10:
                return 0

            reversed_num = reversed_num * 10 + digit

        return sign * reversed_num
