# 2516. Take K of Each Character From Left and Right

# Sliding Window
# Runtime: 17ms

# Complexity:
# + Time: O(n)
# + Space: O(1)


class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        if k == 0:
            return 0

        n = len(s)
        count = [0] * 3

        for c in s:
            count[ord(c) - ord("a")] += 1

        if any(c < k for c in count):
            return -1

        window_count = [0] * 3
        max_window_size = 0
        left = 0

        for right in range(n):
            window_count[ord(s[right]) - ord("a")] += 1

            while any(count[i] - window_count[i] < k for i in range(3)):
                window_count[ord(s[left]) - ord("a")] -= 1
                left += 1

            max_window_size = max(max_window_size, right - left + 1)

        return n - max_window_size
