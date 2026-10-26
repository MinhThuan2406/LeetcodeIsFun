# 3174. Clear Digits
# Difficulty: Easy

# Stack
# Runtime: 2ms (10/02/2025 | 11pm - GMT+7)

# Complexity:
# + Time: O(n)
# + Space: O(n)


class Solution:
    def clearDigits(self, s: str) -> str:
        stk = []
        for c in s:
            if c.isdigit():
                if stk:
                    stk.pop()
            else:
                stk.append(c)
        return "".join(stk)
