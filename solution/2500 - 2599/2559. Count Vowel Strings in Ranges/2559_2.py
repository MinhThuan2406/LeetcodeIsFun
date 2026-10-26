# 2559. Count Vowel Strings in Ranges

# 2nd Approach
# DSs: ArrayList, Set, Array    
# As: Vowel Checking, Binary Search  
# Runtime: 36ms

# Complexity:
# + Time: O(n + m * log k)
# + Space: O(k + m)

import bisect
from typing import List


class Solution:
    def vowelStrings(
        self, words: List[str], queries: List[List[int]]
    ) -> List[int]:
        vowels = set("aeiou")
        valid_indices = [
            i for i, w in enumerate(words) if w[0] in vowels and w[-1] in vowels
        ]

        ans = []
        for l, r in queries:
            count = bisect.bisect_right(valid_indices, r) - bisect.bisect_left(
                valid_indices, l
            )
            ans.append(count)

        return ans
