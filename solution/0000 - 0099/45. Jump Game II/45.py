# 45. Jump Game II | Medium
# https://leetcode.com/problems/jump-game-ii/
# Methods (keyword): Greedy
# Complexity:
# + Time: O(n)
# + Space: O(1)

class Solution:
    def jump(self, nums: list[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0

        jumps = 0
        current_end = 0
        farthest = 0

        for i in range(n - 1):
            farthest = max(farthest, i + nums[i])

            if i == current_end:
                jumps += 1
                current_end = farthest

                if current_end >= n - 1:
                    break
        return jumps
