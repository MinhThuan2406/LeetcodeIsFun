# 2567. Minimum Score by Changing Two Elements | Medium
# https://leetcode.com/problems/minimum-score-by-changing-two-elements/
# Methods (keyword): Greedy, Selection of k extremes
# Complexity:
# + Time: O(N)
# + Space: O(1)

class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        inf = float("inf")
        lo = [inf, inf, inf]
        hi = [-inf, -inf, -inf]
        for v in nums:
            if v < lo[2]:
                lo[2] = v
                if lo[2] < lo[1]: lo[1], lo[2] = lo[2], lo[1]
                if lo[1] < lo[0]: lo[0], lo[1] = lo[1], lo[0]
            if v > hi[2]:
                hi[2] = v
                if hi[2] > hi[1]: hi[1], hi[2] = hi[2], hi[1]
                if hi[1] > hi[0]: hi[0], hi[1] = hi[1], hi[0]
        return min(hi[0] - lo[2], hi[1] - lo[1], hi[2] - lo[0])
