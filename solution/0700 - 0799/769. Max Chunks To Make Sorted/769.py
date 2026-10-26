# 769. Max Chunks To Make Sorted

# Normal Iteration
# Runtime: 1ms

# Complexity:
# + Time: O(n)
# + Space: O(1)

from typing import List


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        mx = 0
        chunks = 0

        for i, val in enumerate(arr):
            mx = max(mx, val)
            if mx == i:
                chunks += 1

        return chunks
