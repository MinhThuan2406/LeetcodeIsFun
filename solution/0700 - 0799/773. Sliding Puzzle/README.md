---
Difficulty: Hard
Utilizable DSAs:
    - Breadth-First Search
    - Array
    - Matrix
---

<!-- problem:start -->
# [773. Sliding Puzzle](https://leetcode.com/problems/sliding-puzzle)

## Description
<!-- description:start -->
<p>On an <code>2 x 3</code> board, there are five tiles labeled from <code>1</code> to <code>5</code>, and an empty square represented by <code>0</code>. A <strong>move</strong> consists of choosing <code>0</code> and a 4-directionally adjacent number and swapping it.</p>
<p>The state of the board is solved if and only if the board is <code>[[1,2,3],[4,5,0]]</code>.</p>
<p>Given the puzzle board <code>board</code>, return <em>the least number of moves required so that the state of the board is solved</em>. If it is impossible for the state of the board to be solved, return <code>-1</code>.</p>

<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0700-0799/0773.Sliding%20Puzzle/images/slide1-grid.jpg" style="width: 244px; height: 165px;" />
<pre>
<strong>Input:</strong> board = [[1,2,3],[4,0,5]]
<strong>Output:</strong> 1
<strong>Explanation:</strong> Swap the 0 and the 5 in one move.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0700-0799/0773.Sliding%20Puzzle/images/slide2-grid.jpg" style="width: 244px; height: 165px;" />
<pre>
<strong>Input:</strong> board = [[1,2,3],[5,4,0]]
<strong>Output:</strong> -1
<strong>Explanation:</strong> No number of moves will make the board solved.
</pre>

<p><strong class="example">Example 3:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0700-0799/0773.Sliding%20Puzzle/images/slide3-grid.jpg" style="width: 244px; height: 165px;" />
<pre>
<strong>Input:</strong> board = [[4,1,2],[5,0,3]]
<strong>Output:</strong> 5
<strong>Explanation:</strong> 5 is the smallest number of moves that solves the board.
An example path:
After move 0: [[4,1,2],[5,0,3]]
After move 1: [[4,1,2],[0,5,3]]
After move 2: [[0,1,2],[4,5,3]]
After move 3: [[1,0,2],[4,5,3]]
After move 4: [[1,2,0],[4,5,3]]
After move 5: [[1,2,3],[4,5,0]]
</pre>

<p><strong>Constraints:</strong></p>
<ul>
	<li><code>board.length == 2</code></li>
	<li><code>board[i].length == 3</code></li>
	<li><code>0 &lt;= board[i][j] &lt;= 5</code></li>
	<li>Each value <code>board[i][j]</code> is <strong>unique</strong>.</li>
</ul>

<!-- description:end -->


## Solutions
<!-- solution:start -->
<!-- tabs:start -->
#### Python
```python
# 773. Sliding Puzzle

# Breadth-First Search, Array, Matrix
# Runtime: 12ms

# Complexity:
# + Time: O(720)
# + Space: O(720)

from collections import deque
from typing import List


class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        start = ''.join(str(board[i][j]) for i in range(2) for j in range(3))
        end = '123450'
        if start == end:
            return 0

        moves = {
            0: [1, 3],
            1: [0, 2, 4],
            2: [1, 5],
            3: [0, 4],
            4: [1, 3, 5],
            5: [2, 4],
        }

        q = deque([start])
        vis = {start}
        ans = 0

        while q:
            ans += 1
            for _ in range(len(q)):
                cur = q.popleft()
                idx0 = cur.index('0')
                chars = list(cur)
                for nxt in moves[idx0]:
                    chars[idx0], chars[nxt] = chars[nxt], chars[idx0]
                    nxt_str = ''.join(chars)
                    if nxt_str == end:
                        return ans
                    if nxt_str not in vis:
                        vis.add(nxt_str)
                        q.append(nxt_str)
                    chars[idx0], chars[nxt] = chars[nxt], chars[idx0]

        return -1
```

<!-- tabs:end -->
<!-- solution:end -->
<!-- problem:end -->
