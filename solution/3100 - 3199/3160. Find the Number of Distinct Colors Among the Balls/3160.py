# 3160. Find the Number of Distinct Colors Among the Balls
# Difficulty: Medium

# Hash Maps
# Runtime: 50ms (07/02/2025 | 10pm - GMT+7)

# Complexity:
# + Time: O(m)
# + Space: O(m)

from collections import defaultdict
from typing import List


class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        ball_to_color = {}
        color_count = defaultdict(int)
        result = []

        for ball, new_color in queries:
            color_count[new_color] += 1

            if ball in ball_to_color:
                old_color = ball_to_color[ball]
                color_count[old_color] -= 1
                if color_count[old_color] == 0:
                    del color_count[old_color]

            ball_to_color[ball] = new_color
            result.append(len(color_count))

        return result
