# 3152. Special Array II

# Record the Leftmost Special Array Position for Each Position
# Runtime: 2ms

# Complexity:
# + Time: O(n)
# + Space: O(n)

from typing import List


class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        n = len(nums)
        d = [0] * n

        for i in range(1, n):
            if nums[i] % 2 != nums[i - 1] % 2:
                d[i] = d[i - 1]
            else:
                d[i] = i

        return [d[r] <= l for l, r in queries]
