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
        # Frequency array for 26 uppercase letters, initialized to zero.
        freq = [0] * 26

        # Populate the frequency array based on the input string.
        for c in tiles:
            freq[ord(c) - ord("A")] += 1

        # Start the backtracking process to count valid sequences.
        return self._backtrack(freq)

    # Helper method: returns the count of valid sequences that can be formed
    # given the current frequency of letters.
    def _backtrack(self, freq: list[int]) -> int:
        count = 0

        # Try each letter from 'A' to 'Z'.
        for i in range(26):
            # Check if the current letter is available to use.
            if freq[i] > 0:
                # Use letter i: count this as one valid sequence.
                count += 1
                # Choose letter i by decrementing its count.
                freq[i] -= 1

                # Recurse to form longer sequences with the remaining letters.
                count += self._backtrack(freq)

                # Backtrack: restore the count for letter i to explore other combinations.
                freq[i] += 1

        # Return the total count of valid sequences found.
        return count
