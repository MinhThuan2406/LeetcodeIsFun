# 2948. Make Lexicographically Smallest Array by Swapping Elements
# Difficulty: Medium

# Sorting, Connected Components
# Runtime: 55ms (25/01/2025 | 11pm - GMT+7)

# Complexity:
# + Time: O(n * log(n))
# + Space: O(n)

from typing import List


class Solution:
    def lexicographicallySmallestArray(
        self, nums: List[int], limit: int
    ) -> List[int]:
        n = len(nums)
        idx = list(range(n))
        idx.sort(key=lambda i: nums[i])

        ans = [0] * n
        i = 0
        while i < n:
            j = i + 1
            while j < n and nums[idx[j]] - nums[idx[j - 1]] <= limit:
                j += 1

            positions = sorted(idx[i:j])
            for k in range(i, j):
                ans[positions[k - i]] = nums[idx[k]]

            i = j

        return ans
