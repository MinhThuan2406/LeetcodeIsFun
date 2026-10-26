# 2337. Move Pieces to Obtain a String

# Two-Pointer
# 36ms

# Complexity:
# + Time: O(n)
# + Space: O(n)


class Solution:
    def canChange(self, start: str, target: str) -> bool:
        start_positions = [(ch, i) for i, ch in enumerate(start) if ch in "LR"]
        target_positions = [(ch, i) for i, ch in enumerate(target) if ch in "LR"]

        if len(start_positions) != len(target_positions):
            return False

        for (s_ch, s_i), (t_ch, t_i) in zip(start_positions, target_positions):
            if s_ch != t_ch:
                return False
            if s_ch == "L" and s_i < t_i:
                return False
            if s_ch == "R" and s_i > t_i:
                return False

        return True
