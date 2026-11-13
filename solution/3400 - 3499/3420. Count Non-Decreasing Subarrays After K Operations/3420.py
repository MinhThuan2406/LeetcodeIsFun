# 3420. Count Non-Decreasing Subarrays After K Operations | Hard
# https://leetcode.com/problems/count-non-decreasing-subarrays-after-k-operations/
# Sliding Window, Monotonic Stack
# Complexity:
# + Time: O(n)
# + Space: O(n)

from collections import deque
from typing import List

class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
        nums = nums[::-1]
        n = len(nums)
        dq = deque()
        cost = 0
        l = 0
        ans = 0

        for r in range(n):
            while dq and nums[dq[-1]] < nums[r]:
                idx = dq.pop()
                left_boundary = dq[-1] if dq else l - 1
                cost += (nums[r] - nums[idx]) * (idx - left_boundary)

            dq.append(r)

            while cost > k:
                cost -= nums[dq[0]] - nums[l]
                if dq[0] == l:
                    dq.popleft()
                l += 1

            ans += r - l + 1

        return ans
