# 1346. Check If N and Its Double Exist

# Brute Force / Hash Set
# Runtime: 2ms

# Complexity:
# + Time: O(n^2)
# + Space: O(1)

from typing import List


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        n = len(arr)
        for i in range(n):
            for j in range(n):
                if i != j and arr[i] == 2 * arr[j]:
                    return True
        return False
