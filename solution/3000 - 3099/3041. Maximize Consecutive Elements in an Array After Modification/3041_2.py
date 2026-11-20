# 2nd method
# 3041. Maximize Consecutive Elements in an Array After Modification | Medium
# https://leetcode.com/problems/maximize-consecutive-elements-in-an-array-after-modification/
# Methods (keyword): Counting Sort, Dynamic Programming
# Complexity:
# + Time: O(n + M)
# + Space: O(M)

class Solution:
    def maxSelectedElements(self, nums: List[int]) -> int:
        M = max(nums)
        cnt = [0] * (M + 1)
        for x in nums:
            cnt[x] += 1

        dp = [0] * (M + 2)
        ans = 0

        for v in range(1, M + 1):
            for _ in range(cnt[v]):
                dp[v + 1] = dp[v] + 1
                dp[v] = dp[v - 1] + 1
                ans = max(ans, dp[v], dp[v + 1])

        return ans
