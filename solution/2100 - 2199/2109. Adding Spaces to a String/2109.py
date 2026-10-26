# 2109. Adding Spaces to a String

# String
# Runtime: 22ms

# Complexity:
# + Time: O(n + m)
# + Space: O(n + m)

from typing import List


class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        res = []
        space_idx = 0
        n = len(spaces)

        for i, ch in enumerate(s):
            if space_idx < n and i == spaces[space_idx]:
                res.append(" ")
                space_idx += 1
            res.append(ch)

        return "".join(res)
