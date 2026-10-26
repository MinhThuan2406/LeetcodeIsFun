# 3254. Find the Power of K-Size Subarrays I
# Brute Force
# Runtime: 2ms

# Complexity
# + Time: O(n * k)
# + Space: O(n - k + 1)

from typing import List


class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        results = []

        for i in range(n - k + 1):
            max_val = float("-inf")
            is_consecutive = True
            prev = nums[i] - 1

            for j in range(i, i + k):
                if nums[j] != prev + 1:
                    is_consecutive = False
                    break
                max_val = max(max_val, nums[j])
                prev = nums[j]

            results.append(max_val if is_consecutive else -1)

        return results
