# 20. Valid Parentheses | Easy
# https://leetcode.com/problems/valid-parentheses/

# Stack
# Runtime: 1ms (27/10/2026 | 9am - GMT+7)

# Complexity:
# + Time: O(n)
# + Space: O(n)

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', '}': '{',']': '['}

        for char in s:
            if char in mapping:
                top_element = stack.pop() if stack else '#'
                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)

        return not stack
