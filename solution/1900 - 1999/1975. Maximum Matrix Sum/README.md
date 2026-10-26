---
Difficulty: Medium
Utilizable DSAs:
    - Greedy
    - Array
    - Matrix
---

<!-- problem:start -->
# [1975. Maximum Matrix Sum](https://leetcode.com/problems/maximum-matrix-sum)

## Description
<!-- description:start -->
<p>You are given an <code>n x n</code> integer <code>matrix</code>. You can do the following operation <strong>any</strong> number of times:</p>
<ul>
	<li>Choose any two <strong>adjacent</strong> elements of <code>matrix</code> and <strong>multiply</strong> each of them by <code>-1</code>.</li>
</ul>
<p>Two elements are considered <strong>adjacent</strong> if and only if they share a <strong>border</strong>.</p>
<p>Your goal is to <strong>maximize</strong> the summation of the matrix&#39;s elements. Return <em>the <strong>maximum</strong> sum of the matrix&#39;s elements using the operation mentioned above.</em></p>

<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/1900-1999/1975.Maximum%20Matrix%20Sum/images/pc79-q2ex1.png" style="width: 401px; height: 81px;" />
<pre>
<strong>Input:</strong> matrix = [[1,-1],[-1,1]]
<strong>Output:</strong> 4
<b>Explanation:</b> We can follow the following steps to reach sum equals 4:
- Multiply the 2 elements in the first row by -1.
- Multiply the 2 elements in the first column by -1.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/1900-1999/1975.Maximum%20Matrix%20Sum/images/pc79-q2ex2.png" style="width: 321px; height: 121px;" />
<pre>
<strong>Input:</strong> matrix = [[1,2,3],[-1,-2,-3],[1,2,3]]
<strong>Output:</strong> 16
<b>Explanation:</b> We can follow the following step to reach sum equals 16:
- Multiply the 2 last elements in the second row by -1.
</pre>

<p><strong>Constraints:</strong></p>
<ul>
	<li><code>n == matrix.length == matrix[i].length</code></li>
	<li><code>2 &lt;= n &lt;= 250</code></li>
	<li><code>-10<sup>5</sup> &lt;= matrix[i][j] &lt;= 10<sup>5</sup></code></li>
</ul>

<!-- description:end -->


## Solutions
<!-- solution:start -->
<!-- tabs:start -->

#### Python
```python
# 1975. Maximum Matrix Sum

# Array, Matrix
# Runtime: 5ms

# Complexity:
# + Time: O(n^2)
# + Space: O(1)

from typing import List


class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        total_sum = 0
        negative_count = 0
        min_abs_value = float("inf")

        for row in matrix:
            for val in row:
                abs_val = abs(val)
                total_sum += abs_val
                if val < 0:
                    negative_count += 1
                if abs_val < min_abs_value:
                    min_abs_value = abs_val

        if negative_count & 1:
            total_sum -= 2 * min_abs_value

        return total_sum
```

<!-- tabs:end -->
<!-- solution:end -->
<!-- problem:end -->
