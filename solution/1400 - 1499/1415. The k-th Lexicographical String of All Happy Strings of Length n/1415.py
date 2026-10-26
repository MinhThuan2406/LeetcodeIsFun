# 1415. The k-th Lexicographical String of All Happy Strings of Length n | Medium
# https://leetcode.com/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n/

# ArrayList, String | Backtracking (Recursive Generation)
# Runtime: 9ms (19/02/2025 | 9pm - GMT+7)

# Complexity:
# + Time: O(3^n) - 3 choices for each character
# + Space: O(n)


class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        count = 0
        result = ""

        def backtrack(s: str) -> None:
            nonlocal count, result
            if len(s) == n:
                count += 1
                if count == k:
                    result = s
                return

            if count >= k:
                return

            for c in ["a", "b", "c"]:
                if not s or s[-1] != c:
                    backtrack(s + c)

        backtrack("")
        return result
