# 2375. Construct Smallest Number From DI String | Medium
# https://leetcode.com/problems/construct-smallest-number-from-di-string/

# Stack | Greedy Approach
# Runtime: 1ms (19/02/2025 | 1am - GMT+7)

# Complexity:
# + Time: O(n) 
# + Space: O(n) 
# with n is the length of the pattern


class Solution:
    def smallestNumber(self, pattern: str) -> str:
        result = []
        stack = []
        n = len(pattern)

        for i in range(n + 1):
            stack.append(str(i + 1))
            if i == n or pattern[i] == "I":
                while stack:
                    result.append(stack.pop())

        return "".join(result)
