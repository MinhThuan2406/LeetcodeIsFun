# 2429. Minimize XOR

# Priority Queue / Bit Manipulation
# Greedy Approach
# Runtime: 2ms (16/1/2025 GMT+7)

# Complexity:
# + Time: O(1)
# + Space: O(1)


class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        cnt = bin(num2).count("1")

        # Collect bit positions of 1s in num1
        bit_positions = [i for i in range(31) if (num1 >> i) & 1]
        bit_positions.sort(reverse=True)

        x = 0
        for pos in bit_positions:
            if cnt <= 0:
                break
            x |= 1 << pos
            cnt -= 1

        # If more bits are needed, set from least significant unset bit
        for i in range(32):
            if cnt <= 0:
                break
            if not ((x >> i) & 1):
                x |= 1 << i
                cnt -= 1

        return x
