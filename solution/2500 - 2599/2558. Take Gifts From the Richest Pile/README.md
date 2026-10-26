---
Difficulty: Easy
Utilizable DSAs/Methods/Approaches:
    - Array
    - Simulation
    - Heap (Priority Queue)
---

<!-- problem:start -->
# [2558. Take Gifts From the Richest Pile](https://leetcode.com/problems/take-gifts-from-the-richest-pile)
## Description
<!-- description:start -->
<p>You are given an integer array <code>gifts</code> denoting the number of gifts in various piles. Every second, you do the following:</p>
<ul>
	<li>Choose the pile with the maximum number of gifts.</li>
	<li>If there is more than one pile with the maximum number of gifts, choose any.</li>
	<li>Leave behind the floor of the square root of the number of gifts in the pile. Take the rest of the gifts.</li>
</ul>
<p>Return <em>the number of gifts remaining after </em><code>k</code><em> seconds.</em></p>

### Examples
<p><strong class="example">1.</strong></p>
<pre>
<strong>Input:</strong> gifts = [25,64,9,4,100], k = 4
<strong>Output:</strong> 29
<strong>Explanation:</strong> 
The gifts are taken in the following way:
- In the first second, the last pile is chosen and 10 gifts are left behind.
- Then the second pile is chosen and 8 gifts are left behind.
- After that the first pile is chosen and 5 gifts are left behind.
- Finally, the last pile is chosen again and 3 gifts are left behind.
The final remaining gifts are [5,8,9,4,3], so the total number of gifts remaining is 29.
</pre>

<p><strong class="example">2.</strong></p>
<pre>
<strong>Input:</strong> gifts = [1,1,1,1], k = 4
<strong>Output:</strong> 4
<strong>Explanation:</strong> 
In this case, regardless which pile you choose, you have to leave behind 1 gift in each pile. 
That is, you can&#39;t take any pile with you. 
So, the total gifts remaining are 4.
</pre>

### Constraints
<ul>
	<li><code>1 &lt;= gifts.length &lt;= 10<sup>3</sup></code></li>
	<li><code>1 &lt;= gifts[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>1 &lt;= k &lt;= 10<sup>3</sup></code></li>
</ul>
<!-- description:end -->


<p>&nbsp;</p>


## Solutions
<!-- solution:start -->
<!-- tabs:start -->
#### Python
```python
# 2558. Take Gifts From the Richest Pile

# Max-Heap Priority Queue
# Runtime: 6ms

# Complexity:
# + Time: O(k * log(n) + n)
# + Space: O(n)

import heapq
import math
from typing import List


class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        max_heap = [-g for g in gifts]
        heapq.heapify(max_heap)

        for _ in range(k):
            largest = -heapq.heappop(max_heap)
            heapq.heappush(max_heap, -int(math.isqrt(largest)))

        return -sum(max_heap)
```
<!-- tabs:end -->
<!-- solution:end -->
<!-- problem:end -->
