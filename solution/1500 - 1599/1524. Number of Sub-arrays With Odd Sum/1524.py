# 1524. Number of Sub-arrays With Odd Sum | Medium
# https://leetcode.com/problems/number-of-sub-arrays-with-odd-sum/
# Methods (keyword): Prefix Sum, Counting
# Complexity:
# + Time: O(n)
# + Space: O(1)

class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        MOD = 10**9 + 7

        even_count = 1
        odd_count = 0
        curr_sum = 0
        ans = 0

        for num in arr:
            curr_sum += num

            if curr_sum % 2 == 1:
                ans += even_count
                odd_count += 1
            else:
                ans += odd_count
                even_count += 1

        return ans % MOD
