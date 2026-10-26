<!-- problem:start -->
# [2559. Count Vowel Strings in Ranges](https://leetcode.com/problems/count-vowel-strings-in-ranges)

## Solutions
<!-- solution:start -->
### 1/ Prefix Sum Array, Range Query Handling
<!-- tabs:start -->
##### Python
```python
# 2559. Count Vowel Strings in Ranges

# 1st Approach
# Prefix Sum Array, Range Query Handling
# Runtime: 6ms

# Complexity:
# + Time: O(n + m)
# + Space: O(n + m)

from typing import List


class Solution:
    def vowelStrings(
        self, words: List[str], queries: List[List[int]]
    ) -> List[int]:
        vowels = set("aeiou")
        n = len(words)
        valid = [1 if words[i][0] in vowels and words[i][-1] in vowels else 0 for i in range(n)]

        prefix = [0] * n
        prefix[0] = valid[0]
        for i in range(1, n):
            prefix[i] = prefix[i - 1] + valid[i]

        result = []
        for li, ri in queries:
            result.append(prefix[ri] - (prefix[li - 1] if li > 0 else 0))

        return result
```
<!-- tabs:end -->


<p>&nbsp;</p>


### 2/ Preprocessing + Binary Search
<!-- tabs:start -->
##### Python
```python
# 2559. Count Vowel Strings in Ranges

# 1st Approach
# Prefix Sum Array, Range Query Handling
# Runtime: 6ms

# Complexity:
# + Time: O(n + m)
# + Space: O(n + m)

from typing import List


class Solution:
    def vowelStrings(
        self, words: List[str], queries: List[List[int]]
    ) -> List[int]:
        vowels = set("aeiou")
        n = len(words)
        valid = [1 if words[i][0] in vowels and words[i][-1] in vowels else 0 for i in range(n)]

        prefix = [0] * n
        prefix[0] = valid[0]
        for i in range(1, n):
            prefix[i] = prefix[i - 1] + valid[i]

        result = []
        for li, ri in queries:
            result.append(prefix[ri] - (prefix[li - 1] if li > 0 else 0))

        return result
```
<!-- tabs:end -->
<!-- solution:end -->
<!-- problem:end -->
