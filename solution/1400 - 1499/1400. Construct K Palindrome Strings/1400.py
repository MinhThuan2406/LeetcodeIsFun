# 1400. Construct K Palindrome Strings

# Array, Frequency Counting
# Runtime: 4ms

# Complexity:
# + Time: O(n)
# + Space: O(1)


class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False

        cnt = [0] * 26
        for c in s:
            cnt[ord(c) - ord("a")] += 1

        odd_count = sum(v & 1 for v in cnt)
        return odd_count <= k
