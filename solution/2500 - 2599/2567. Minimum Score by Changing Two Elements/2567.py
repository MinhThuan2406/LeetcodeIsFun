# 2567. Minimum Score by Changing Two Elements | Medium
# https://leetcode.com/problems/minimum-score-by-changing-two-elements/
# Methods (keyword): Sorting, Greedy
# Complexity:
# + Time: O(N log N)
# + Space: O(1) (ignoring the O(log N) sorting stack; in-place sort)

class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        nums.sort()
        return min(nums[-1] - nums[2], nums[-2] - nums[1], nums[-3] - nums[0])
