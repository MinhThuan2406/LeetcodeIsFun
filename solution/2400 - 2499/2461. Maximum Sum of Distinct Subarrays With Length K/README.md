---
Difficulty: Medium
Potential DSAs for this problem:
    - Array
    - Hash Table
    - Sliding Window
---

<!-- problem:start -->

# [2461. Maximum Sum of Distinct Subarrays With Length K](https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k)
## Description
<!-- description:start -->
<p>You are given an integer array <code>nums</code> and an integer <code>k</code>. Find the maximum subarray sum of all the subarrays of <code>nums</code> that meet the following conditions:</p>
<ul>
	<li>The length of the subarray is <code>k</code>, and</li>
	<li>All the elements of the subarray are <strong>distinct</strong>.</li>
</ul
<p>Return <em>the maximum subarray sum of all the subarrays that meet the conditions</em><em>.</em> If no subarray meets the conditions, return <code>0</code>.</p>
<p><em>A <strong>subarray</strong> is a contiguous non-empty sequence of elements within an array.</em></p>

<p><strong class="example">Example 1:</strong></p>
<pre>
<strong>Input:</strong> nums = [1,5,4,2,9,9,9], k = 3
<strong>Output:</strong> 15
<strong>Explanation:</strong> The subarrays of nums with length 3 are:
- [1,5,4] which meets the requirements and has a sum of 10.
- [5,4,2] which meets the requirements and has a sum of 11.
- [4,2,9] which meets the requirements and has a sum of 15.
- [2,9,9] which does not meet the requirements because the element 9 is repeated.
- [9,9,9] which does not meet the requirements because the element 9 is repeated.
We return 15 because it is the maximum subarray sum of all the subarrays that meet the conditions
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre>
<strong>Input:</strong> nums = [4,4,4], k = 3
<strong>Output:</strong> 0
<strong>Explanation:</strong> The subarrays of nums with length 3 are:
- [4,4,4] which does not meet the requirements because the element 4 is repeated.
We return 0 because no subarrays meet the conditions.
</pre>

<p><strong>Constraints:</strong></p>
<ul>
	<li><code>1 &lt;= k &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
</ul>
<!-- description:end -->


## Solutions
<!-- solution:start -->
<!-- tabs:start -->
#### Python
```python
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
```

<!-- tabs:end -->
<!-- solution:end -->
<!-- problem:end -->
