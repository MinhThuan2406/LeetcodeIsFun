# 1455. Check If a Word Occurs As a Prefix of Any Word in a Sentence

# Split & Iterate
# Runtime: 0ms

# Complexity:
# + Time: O(n)
# + Space: O(n)


class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        words = sentence.split(" ")
        for i, word in enumerate(words):
            if word.startswith(searchWord):
                return i + 1
        return -1
