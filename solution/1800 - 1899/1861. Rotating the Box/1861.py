# 1861. Rotate the Box

# Queue / Two Pointers
# Runtime: 20ms

# Complexity:
# + Time: O(m * n)
# + Space: O(m * n)
# m is the number of rows in the original box
# n is the number of columns in the original box

from collections import deque
from typing import List


class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        m, n = len(box), len(box[0])
        ans = [[""] * m for _ in range(n)]

        for i in range(m):
            for j in range(n):
                ans[j][m - i - 1] = box[i][j]

        for j in range(m):
            q = deque()
            for i in range(n - 1, -1, -1):
                if ans[i][j] == "*":
                    q.clear()
                elif ans[i][j] == ".":
                    q.append(i)
                elif q:
                    empty_idx = q.popleft()
                    ans[empty_idx][j] = "#"
                    ans[i][j] = "."
                    q.append(i)

        return ans
