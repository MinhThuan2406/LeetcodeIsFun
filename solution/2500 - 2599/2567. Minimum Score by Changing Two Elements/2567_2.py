# 2567. Minimum Score by Changing Two Elements | Medium
# https://leetcode.com/problems/minimum-score-by-changing-two-elements/
# Methods (keyword): Greedy, Selection of k extremes
# Complexity:
# + Time: O(N)
# + Space: O(1)

import heapq

class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        a, b, c = heapq.nsmallest(3, nums)  # a <= b <= c
        z, y, x = heapq.nlargest(3, nums)   # z >= y >= x
        return min(z - c, y - b, x - a)
