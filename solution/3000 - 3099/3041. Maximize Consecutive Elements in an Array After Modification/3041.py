# 3041. Maximize Consecutive Elements in an Array After Modification | Medium
# https://leetcode.com/problems/maximize-consecutive-elements-in-an-array-after-modification/
# Methods (keyword): Hash Map, Dynamic Programming, Sorting
# Complexity:
# + Time: O(n log n)
# + Space: O(n)

class Solution:
    def maxSelectedElements(self, nums: List[int]) -> int:
        nums.sort()

        dp = {}
        ans = 0

        for i in nums:
            dp[i + 1] = dp.get(i, 0) + 1
            dp[i] = dp.get(i - 1, 0) + 1
            ans = max(ans, dp[i + 1], dp[i])

        return ans
