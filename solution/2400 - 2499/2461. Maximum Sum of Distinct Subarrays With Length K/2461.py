# 2461. Maximum Sum of Distinct Subarrays With Length K

# HashSet, Sliding Window
# Runtime: 33ms

# Complexity
# + Time: O(n)
# + Space: O(k)

from typing import List


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        max_sum = 0
        current_sum = 0
        unique_elements = set()

        start = 0
        for end in range(len(nums)):
            current_sum += nums[end]

            while nums[end] in unique_elements:
                current_sum -= nums[start]
                unique_elements.remove(nums[start])
                start += 1

            unique_elements.add(nums[end])

            if end - start + 1 == k:
                max_sum = max(max_sum, current_sum)
                current_sum -= nums[start]
                unique_elements.remove(nums[start])
                start += 1

        return max_sum
