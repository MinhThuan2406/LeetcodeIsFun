---
Difficulty: Easy
Utilizable DSAs/Methods/Approaches:
    - Array
    - Hash Table
    - Two Pointers
    - Binary Search
    - Sorting
    - Brute Force
---


<!-- problem:start -->
# [1346. Check If N and Its Double Exist](https://leetcode.com/problems/check-if-n-and-its-double-exist)

## Description
<!-- description:start -->
<p>Given an array <code>arr</code> of integers, check if there exist two indices <code>i</code> and <code>j</code> such that :</p>
<ul>
	<li><code>i != j</code></li>
	<li><code>0 &lt;= i, j &lt; arr.length</code></li>
	<li><code>arr[i] == 2 * arr[j]</code></li>
</ul>

### Examples
<p><strong class="example">1.</strong></p>
<pre>
<strong>Input:</strong> arr = [10,2,5,3]
<strong>Output:</strong> true
<strong>Explanation:</strong> For i = 0 and j = 2, arr[i] == 10 == 2 * 5 == 2 * arr[j]
</pre>

<p><strong class="example">2.</strong></p>
<pre>
<strong>Input:</strong> arr = [3,1,7,11]
<strong>Output:</strong> false
<strong>Explanation:</strong> There is no i and j that satisfy the conditions.
</pre>

### Constraints
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>2 &lt;= arr.length &lt;= 500</code></li>
	<li><code>-10<sup>3</sup> &lt;= arr[i] &lt;= 10<sup>3</sup></code></li>
</ul>
<!-- description:end -->


<p>&nbsp;</p>


## Solutions
<!-- solution:start -->
##### 1/ Brute Force
<!-- tabs:start -->
##### Python
```python
# 1346. Check If N and Its Double Exist

# Brute Force / Hash Set
# Runtime: 2ms

# Complexity:
# + Time: O(n^2)
# + Space: O(1)

from typing import List


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        n = len(arr)
        for i in range(n):
            for j in range(n):
                if i != j and arr[i] == 2 * arr[j]:
                    return True
        return False
```
<!-- tabs:end -->
<!-- solution:end -->
<!-- problem:end -->
