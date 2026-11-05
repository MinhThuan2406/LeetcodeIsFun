# 1385. Find the Distance Value Between Two Arrays | Easy
# https://leetcode.com/problems/find-the-distance-value-between-two-arrays/
# Array, Two Pointers, Binary Search, Sorting
# Complexity:
# + Time: O((n + m) * log(m))
# + Space: O(m)

import bisect

class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        arr2.sort()
        ans = 0

        for x in arr1:
            idx = bisect.bisect_left(arr2, x - d)

            if idx < len(arr2) and arr2[idx] <= x + d:
                continue

            ans += 1

        return ans
