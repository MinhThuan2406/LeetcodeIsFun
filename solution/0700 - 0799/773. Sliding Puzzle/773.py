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
