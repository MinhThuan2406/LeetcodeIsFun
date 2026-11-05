# 1385. Find the Distance Value Between Two Arrays | Easy
# https://leetcode.com/problems/find-the-distance-value-between-two-arrays/
# Array, Hash Table, Prefix Sum
# Complexity:
# + Time: O(n + m + V), V = range of values = 2001
# + Space: O(V)

class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        LO, HI = -1000, 1000
        V = HI - LO + 1

        diff = [0] * (V + 1)
        for y in arr2:
            l = max(y - d, LO) - LO
            r = min(y + d, HI) - LO
            diff[l] += 1
            diff[r + 1] -= 1

        covered = [False] * V
        cur = 0
        for i in range(V):
            cur += diff[i]
            covered[i] = cur > 0

        return sum(1 for x in arr1 if not covered[x - LO])
