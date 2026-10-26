# 3223. Minimum Length of String After Operations

# Frequency Counting
# Runtime: 9ms

# Complexity:
# + Time: O(n)
# + Space: O(1)

from collections import Counter


class Solution:
    def minimumLength(self, s: str) -> int:
        cnt = Counter(s)
        return sum(1 if v % 2 == 1 else 2 for v in cnt.values())
