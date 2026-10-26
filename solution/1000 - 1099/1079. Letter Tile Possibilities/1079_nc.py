# 1079. Letter Tile Possibilities | Medium
# https://leetcode.com/problems/letter-tile-possibilities/

# Backtracking
# Runtime: 2ms (17/02/2025 | 11pm - GMT+7)

# Complexity:
# + Time: O(26^N)
# + Space: O(N)
# where N is the length of the input string


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        freq = [0] * 26
        for c in tiles:
            freq[ord(c) - ord("A")] += 1
        return self._backtrack(freq)

    def _backtrack(self, freq: list[int]) -> int:
        count = 0
        for i in range(26):
            if freq[i] > 0:
                count += 1
                freq[i] -= 1
                count += self._backtrack(freq)
                freq[i] += 1
        return count
