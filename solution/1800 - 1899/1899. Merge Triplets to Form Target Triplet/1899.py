# 1899. Merge Triplets to Form Target Triplet | Medium
# https://leetcode.com/problems/merge-triplets-to-form-target-triplet/

# Greedy
# Runtime: 0ms (27/10/2026 | 2pm - GMT+7)

# Complexity:
# + Time: O(n)
# + Space: O(1)

class Solution:
    def mergeTriplets(self, triplets: list[list[int]], target: list[int]) -> bool:
        found_x = False
        found_y = False
        found_z = False

        tx, ty, tz = target

        for a, b, c in triplets:
            if a <= tx and b <= ty and c <= tz:
                if a == tx:
                    found_x = True
                if b == ty:
                    found_y = True
                if c == tz:
                    found_z = True

            if found_x and found_y and found_z:
                return True

        return found_x and found_y and found_z
