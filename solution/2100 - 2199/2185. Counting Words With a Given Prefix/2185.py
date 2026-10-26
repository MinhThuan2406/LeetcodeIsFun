# 2185. Counting Words With a Given Prefix

# Brute Force
# Runtime: 0ms (9/1/2025)

# Complexity:
# + Time: O(n * p), n: number of words; p: prefix length
# + Space: O(1)

from typing import List


class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        return sum(1 for word in words if word.startswith(pref))
