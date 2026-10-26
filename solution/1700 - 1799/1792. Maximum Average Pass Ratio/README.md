---
Difficulty: Medium
Utilizable DSAs/Methods/Approaches:
    - Greedy
    - Array
    - Heap (Priority Queue)
---

<!-- problem:start -->
# [1792. Maximum Average Pass Ratio](https://leetcode.com/problems/maximum-average-pass-ratio)
## Description
<!-- description:start -->
<p>There is a school that has classes of students and each class will be having a final exam. You are given a 2D integer array <code>classes</code>, where <code>classes[i] = [pass<sub>i</sub>, total<sub>i</sub>]</code>. You know beforehand that in the <code>i<sup>th</sup></code> class, there are <code>total<sub>i</sub></code> total students, but only <code>pass<sub>i</sub></code> number of students will pass the exam.</p>
<p>You are also given an integer <code>extraStudents</code>. There are another <code>extraStudents</code> brilliant students that are <strong>guaranteed</strong> to pass the exam of any class they are assigned to. You want to assign each of the <code>extraStudents</code> students to a class in a way that <strong>maximizes</strong> the <strong>average</strong> pass ratio across <strong>all</strong> the classes.</p>
<p>The <strong>pass ratio</strong> of a class is equal to the number of students of the class that will pass the exam divided by the total number of students of the class. The <strong>average pass ratio</strong> is the sum of pass ratios of all the classes divided by the number of the classes.</p>
<p>Return <em>the <strong>maximum</strong> possible average pass ratio after assigning the </em><code>extraStudents</code><em> students. </em>Answers within <code>10<sup>-5</sup></code> of the actual answer will be accepted.</p>

### Examples
<p><strong class="example">1.</strong></p>
<pre>
<strong>Input:</strong> classes = [[1,2],[3,5],[2,2]], <code>extraStudents</code> = 2
<strong>Output:</strong> 0.78333
<strong>Explanation:</strong> You can assign the two extra students to the first class. The average pass ratio will be equal to (3/4 + 3/5 + 2/2) / 3 = 0.78333.
</pre>

<p><strong class="example">2.</strong></p>
<pre>
<strong>Input:</strong> classes = [[2,4],[3,9],[4,5],[2,10]], <code>extraStudents</code> = 4
<strong>Output:</strong> 0.53485
</pre>

### Constraints
<ul>
	<li><code>1 &lt;= classes.length &lt;= 10<sup>5</sup></code></li>
	<li><code>classes[i].length == 2</code></li>
	<li><code>1 &lt;= pass<sub>i</sub> &lt;= total<sub>i</sub> &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= extraStudents &lt;= 10<sup>5</sup></code></li>
</ul>
<!-- description:end -->


<p>&nbsp;</p>


## Solution: Priority Queue (Max-Heap) + Greedy Approach
<!-- solution:start -->
Suppose a class currently has a pass rate of $\frac{a}{b}$. If we arrange a smart student into this class, then the pass rate of the class will become $\frac{a+1}{b+1}$. We can find that the increment of the pass rate is $\frac{a+1}{b+1} - \frac{a}{b}$.

We maintain a max-heap, which stores the increment of the pass rate for each class.

Perform `extraStudents` operations, each time taking a class from the top of the heap, adding $1$ to both the number of students and the number of passes in this class, then recalculating the increment of the pass rate of this class and putting it back into the heap. Repeat this process until all students are allocated.

Finally, we sum up the pass rates of all classes, and then divide by the number of classes to get the answer.

The time complexity is $O(n \times \log n)$, and the space complexity is $O(n)$. Here, $n$ is the number of classes.

<!-- tabs:start -->
#### Python
```python
# 1792. Maximum Average Pass Ratio

# Priority Queue (Max-Heap)
# Greedy Approach
# Runtime: 329ms

# Complexity:
# + Time: O(n * log(n))
# + Space: O(n)

import heapq
from typing import List


class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        # Heap elements: (-gain, pass_count, total_count)
        def gain(p: int, t: int) -> float:
            return (p + 1) / (t + 1) - p / t

        max_heap = [(-gain(p, t), p, t) for p, t in classes]
        heapq.heapify(max_heap)

        for _ in range(extraStudents):
            cur_gain, p, t = heapq.heappop(max_heap)
            p += 1
            t += 1
            heapq.heappush(max_heap, (-gain(p, t), p, t))

        return sum(p / t for _, p, t in max_heap) / len(classes)
```
<!-- tabs:end -->
<!-- solution:end -->
<!-- problem:end -->
