# 916. Word Subsets

# Frequency Counting
# Runtime: 15ms

# Complexity:
# + Time: O(m * n)
# + Space: O(1)

from typing import List


class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        target_freq = [0] * 26
        for b in words2:
            freq = [0] * 26
            for c in b:
                idx = ord(c) - ord('a')
                freq[idx] += 1
                target_freq[idx] = max(target_freq[idx], freq[idx])

        def is_universal(a: str) -> bool:
            freq = [0] * 26
            for c in a:
                freq[ord(c) - ord('a')] += 1
            for i in range(26):
                if freq[i] < target_freq[i]:
                    return False
            return True

        return [a for a in words1 if is_universal(a)]
