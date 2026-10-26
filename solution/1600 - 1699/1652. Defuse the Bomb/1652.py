# 1652. Defuse the Bomb

# Array, Sliding Window
# Runtime: 2ms

# Complexity
# + Time: O(n * |k|)
# + Space: O(n)

from typing import List


class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        ans = [0] * n
        if k == 0:
            return ans

        for i in range(n):
            if k > 0:
                for j in range(i + 1, i + k + 1):
                    ans[i] += code[j % n]
            else:
                for j in range(i + k, i):
                    ans[i] += code[(j + n) % n]

        return ans
