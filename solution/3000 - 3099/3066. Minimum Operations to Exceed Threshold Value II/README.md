# [3066. Minimum Operations to Exceed Threshold Value II](https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-ii/)
## Problem Description
Given an array of integers and a threshold value, the task is to find the minimum number of operations required to make the sum of the array elements exceed the threshold. In one operation, you can increment any element of the array by 1.

## Examples
### Example 1
```
Input: nums = [1, 2, 3], threshold = 10
Output: 4
Explanation: Increment the elements as follows: [1, 2, 3] -> [2, 2, 3] -> [3, 2, 3] -> [4, 2, 3] -> [4, 3, 3]. The sum is now 10.
```

### Example 2
```
Input: nums = [1, 1, 1], threshold = 5
Output: 2
Explanation: Increment the elements as follows: [1, 1, 1] -> [2, 1, 1] -> [2, 2, 1]. The sum is now 5.
```

## Constraints
- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^4`
- `1 <= threshold <= 10^9`

## Solution
```python
# 3066. Minimum Operations to Exceed Threshold Value II
# Difficulty: Medium
# Link: https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-ii/

# Priority Queue (Min-Heap)
# Runtime: 148ms (13/02/2025 | 11pm - GMT+7)

# Complexity Analysis
# + Time: O(n * log(n)) where n is the number of elements in the input array.
# + Space: O(n) where n is the number of elements in the input array.

import heapq
from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        ans = 0

        while len(nums) > 1 and nums[0] < k:
            x = heapq.heappop(nums)
            y = heapq.heappop(nums)
            heapq.heappush(nums, 2 * x + y)
            ans += 1

        return ans
```
