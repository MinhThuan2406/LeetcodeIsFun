# 689. Maximum Sum of 3 Non-Overlapping Subarrays

# Fixed-size Sliding Windows
# Runtime: 7ms

# Complexity:
# + Time: O(n)
# + Space: O(1)

from typing import List


class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        ans = [0, 0, 0]
        s = s1 = s2 = s3 = 0
        mx1 = mx12 = 0
        idx1 = idx121 = idx122 = 0

        for i in range(k * 2, len(nums)):
            s1 += nums[i - k * 2]
            s2 += nums[i - k]
            s3 += nums[i]
            if i >= k * 3 - 1:
                if s1 > mx1:
                    mx1 = s1
                    idx1 = i - k * 3 + 1
                if mx1 + s2 > mx12:
                    mx12 = mx1 + s2
                    idx121 = idx1
                    idx122 = i - k * 2 + 1
                if mx12 + s3 > s:
                    s = mx12 + s3
                    ans = [idx121, idx122, i - k + 1]
                s1 -= nums[i - k * 3 + 1]
                s2 -= nums[i - k * 2 + 1]
                s3 -= nums[i - k + 1]

        return ans
