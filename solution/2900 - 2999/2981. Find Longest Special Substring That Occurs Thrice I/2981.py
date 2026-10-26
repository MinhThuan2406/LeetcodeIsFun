# 2981. Find Longest Special Substring That Occurs Thrice I

# Binary Search, Sliding Window
# Runtime: 2ms 

# Complexity:
# + Time: O(n log(n))
# + Space: O(1)


class Solution:
    def maximumLength(self, s: str) -> int:
        n = len(s)

        def check(x: int) -> bool:
            cnt = [0] * 26
            i = 0
            while i < n:
                j = i + 1
                while j < n and s[j] == s[i]:
                    j += 1
                k = ord(s[i]) - ord("a")
                cnt[k] += max(0, j - i - x + 1)
                if cnt[k] >= 3:
                    return True
                i = j
            return False

        l, r = 0, n
        while l < r:
            mid = (l + r + 1) >> 1
            if check(mid):
                l = mid
            else:
                r = mid - 1

        return -1 if l == 0 else l
