# 1760. Minimum Limit of Balls in a Bag

# Binary Search
# Runtime: 27ms

# Complexity:
# + Time: O(n * log(max(nums)))
# + Space: O(1)

from typing import List


class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        def can_distribute(penalty: int) -> bool:
            operations = 0
            for balls in nums:
                if balls > penalty:
                    operations += (balls - 1) // penalty
                if operations > maxOperations:
                    return False
            return True

        left, right = 1, max(nums)
        while left < right:
            mid = left + (right - left) // 2
            if can_distribute(mid):
                right = mid
            else:
                left = mid + 1

        return left
