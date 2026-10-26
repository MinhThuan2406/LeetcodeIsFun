# 862. Shortest Subarray with Sum at Least K

# Queue, Array, Binary Search, Prefix Sum, Sliding Window, Monotonic Queue, Heap (Priority Queue)
# Runtime: 39ms

# Complexity
# + Time: O(n * |k|)
# + Space: O(n)

from collections import deque
from typing import List


class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        s = [0] * (n + 1)
        for i in range(n):
            s[i + 1] = s[i] + nums[i]

        q = deque()
        ans = n + 1

        for i in range(n + 1):
            while q and s[i] - s[q[0]] >= k:
                ans = min(ans, i - q.popleft())
            while q and s[q[-1]] >= s[i]:
                q.pop()
            q.append(i)

        return -1 if ans > n else ans
