<!-- problem:start -->
# [1769. Minimum Number of Operations to Move All Balls to Each Box](https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box)
## Solutions
<!-- solution:start -->
### 1/ Prefix Sum
<!-- tabs:start -->
##### Python
```python
# 1769. Minimum Number of Operations to Move All Balls to Each Box

# Prefix Sum
# Runtime: 3ms

# Complexity:
# + Time: O(n)
# + Space: O(1)

from typing import List


class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        result = [0] * n

        balls = 0
        moves = 0
        # Left to right
        for i in range(n):
            result[i] += moves
            balls += 1 if boxes[i] == "1" else 0
            moves += balls

        balls = 0
        moves = 0
        # Right to left
        for i in range(n - 1, -1, -1):
            result[i] += moves
            balls += 1 if boxes[i] == "1" else 0
            moves += balls

        return result
```


### 2/ Brute Force (not very ideal)
<!-- tabs:start -->
##### Python
```python
# 1769. Minimum Number of Operations to Move All Balls to Each Box

# Prefix Sum
# Runtime: 3ms

# Complexity:
# + Time: O(n)
# + Space: O(1)

from typing import List


class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        result = [0] * n

        balls = 0
        moves = 0
        # Left to right
        for i in range(n):
            result[i] += moves
            balls += 1 if boxes[i] == "1" else 0
            moves += balls

        balls = 0
        moves = 0
        # Right to left
        for i in range(n - 1, -1, -1):
            result[i] += moves
            balls += 1 if boxes[i] == "1" else 0
            moves += balls

        return result
```
<!-- tabs:end -->
<!-- solution:end -->
<!-- problem:end -->
