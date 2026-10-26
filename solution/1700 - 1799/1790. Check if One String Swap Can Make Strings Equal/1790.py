# 1790. Check if One String Swap Can Make Strings Equal
# Difficulty: Easy

# DSAs
# Methods & Approaches
# Runtime: 0ms (05/02/2025 | 8pm - GMT+7)

# Complexity:
# + Time: O(n)
# + Space: O(1)


class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        first, second = -1, -1
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                if first == -1:
                    first = i
                elif second == -1:
                    second = i
                else:
                    return False

        if first == -1:
            return True
        elif second == -1:
            return False
        else:
            return s1[first] == s2[second] and s1[second] == s2[first]
