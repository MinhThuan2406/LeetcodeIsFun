# 1352. Product of the Last K Numbers
# Difficulty: Medium
# Link: https://leetcode.com/problems/product-of-the-last-k-numbers/

# List
# Prefix
# Runtime: 16ms (14/02/2025 | 8pm - GMT+7)

# Complexity:
# + Time: O(1) for add() and O(1) for getProduct()
# + Space: O(n) for prefix list


class ProductOfNumbers:
    def __init__(self):
        # List to store cumulative (prefix) products.
        # We start with an initial value of 1 to simplify multiplication.
        self.prefix = [1]

    def add(self, num: int) -> None:
        # If num is 0, we cannot use previous products,
        # so we clear the list and start fresh.
        if num == 0:
            self.prefix = [1]
        else:
            # Multiply the last product with num and add it.
            self.prefix.append(self.prefix[-1] * num)

    def getProduct(self, k: int) -> int:
        # If k is greater than or equal to the size of the prefix list,
        # that means a 0 was encountered within the last k numbers.
        if k >= len(self.prefix):
            return 0
        # Total product of all numbers so far divided by product before last k.
        return self.prefix[-1] // self.prefix[-1 - k]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
