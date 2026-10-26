<!-- problem:start -->
# [2270. Number of Ways to Split Array](https://leetcode.com/problems/number-of-ways-to-split-array)
## Solutions
<!-- solution:start -->
#### 1/ Prefix and Suffix Sum
<!-- tabs:start -->
##### Python
```python
# 2270. Number of Ways to Split Array

# Prefix and Suffix Sum
# Runtime: 4ms

# Complexity:
# + Time: O(n)
# + Space: O(1)

from typing import List


class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        prefix_sum = 0
        valid_splits = 0

        for i in range(len(nums) - 1):
            prefix_sum += nums[i]
            if prefix_sum >= total_sum - prefix_sum:
                valid_splits += 1

        return valid_splits
```
<!-- tabs:end -->
<!-- solution:end -->
<!-- problem:end -->
