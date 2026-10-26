# 2825. Make String a Subsequence Using Cyclic Increments

# Two-Pointer Greedy Matching
# Runtime: 6ms

# Complexity:
# + Time: O(n + m)
# + Space: O(1)


class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        i, j = 0, 0
        n1, n2 = len(str1), len(str2)

        while i < n1 and j < n2:
            c1, c2 = str1[i], str2[j]
            next_c1 = chr((ord(c1) - ord("a") + 1) % 26 + ord("a"))
            if c1 == c2 or next_c1 == c2:
                j += 1
            i += 1

        return j == n2
