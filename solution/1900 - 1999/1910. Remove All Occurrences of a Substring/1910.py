# 1910. Remove All Occurrences of a Substring
# Difficulty: Medium
# Link: https://leetcode.com/problems/remove-all-occurrences-of-a-substring/

# String
# Runtime: 7ms (11/02/2025 | 1pm - GMT+7)

# Complexity:
# Time: O(n * m) where n is length of s, m is length of part
# Space: O(n) for storing the modified string after each replacement


class Solution:
    """Removes all occurrences of a substring from a string."""

    def removeOccurrences(self, s: str, part: str) -> str:
        while part in s:
            s = s.replace(part, "", 1)
        return s
