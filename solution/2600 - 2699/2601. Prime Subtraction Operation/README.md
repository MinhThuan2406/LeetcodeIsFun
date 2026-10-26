# 2601. Prime Subtraction Operation 

## Problem Statement
Given a 0-indexed integer array `nums`, create an algorithm that makes `nums` strictly increasing by subtracting a prime number from each element at most once. The prime number must be less than the element itself.

### Examples
#### Example 1:
- **Input**: `nums = [4,9,6,10]`
- **Output**: `true`
- **Explanation**:
    - Operation 1: Pick index `0`, prime `3` → `nums[0] = 4 - 3 = 1` → Result: `[1,9,6,10]`
    - Operation 2: Pick index `1`, prime `7` → `nums[1] = 9 - 7 = 2` → Result: `[1,2,6,10]`
    - The final array `[1,2,6,10]` is strictly increasing.

#### Example 2:
- **Input**: `nums = [6,8,11,12]`
- **Output**: `true`
- **Explanation**: The array is already strictly increasing.

#### Example 3:
- **Input**: `nums = [5,8,3]`
- **Output**: `false`
- **Explanation**: It's impossible to make the array strictly increasing with the allowed operations.

## Solution Approach

### Steps
1. **Iterate Through Array**: Track the last modified element (`prev`).
2. **Condition Check**: For each element `nums[i]`, check if it's greater than `prev` (if not, the task is impossible).
3. **Prime Subtraction**:
   - Calculate the maximum value that can be subtracted from `nums[i]` to ensure it stays above `prev`.
   - Find the largest prime number less than or equal to this maximum.
4. **Update Array**: Subtract the prime (if one exists) and update `prev`.

### Helper Functions
#### Prime Validator
Checks if a number is prime:
```python
def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    for i in range(2, int(math.isqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
```

#### Largest Prime Finder
Finds the largest prime number less than a given number:
```python
def find_largest_prime(n: int) -> int:
    for i in range(n - 1, 1, -1):
        if is_prime(i):
            return i
    return 0
```

### Main Function
```python
def primeSubOperation(nums: list[int]) -> bool:
    prev = 0  # Initialize `prev` to track last modified element

    for i in range(len(nums)):
        if nums[i] <= prev:
            return False  # If `nums[i]` is not greater than `prev`, return false

        max_subtract = nums[i] - prev - 1  # Calculate max possible value to subtract

        if max_subtract > 0:
            prime = find_largest_prime(max_subtract + 1)  # Find largest prime within limit
            if prime > 0:
                nums[i] -= prime  # Subtract prime if found

        prev = nums[i]  # Update `prev` to current element

    return True
```
### Full Code
```python
import math
from typing import List


class Solution:
    def _is_prime(self, n: int) -> bool:
        if n <= 1:
            return False
        for i in range(2, int(math.isqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    def _find_largest_prime(self, n: int) -> int:
        for i in range(n - 1, 1, -1):
            if self._is_prime(i):
                return i
        return 0

    def primeSubOperation(self, nums: List[int]) -> bool:
        prev = 0

        for i in range(len(nums)):
            if nums[i] <= prev:
                return False

            max_subtract = nums[i] - prev - 1
            if max_subtract > 0:
                prime = self._find_largest_prime(max_subtract + 1)
                nums[i] -= prime

            prev = nums[i]

        return True
```

## Complexity Analysis
- **Time Complexity**: `O(n * m * √m)`
    - `n`: Length of array
    - `m`: Maximum number in array
    - `√m`: Checking for prime numbers
- **Space Complexity**: `O(1)`: Uses constant extra space.
- **Overall Runtime**: 3ms

## Constraints
- `1 ≤ nums.length ≤ 1000`
- `1 ≤ nums[i] ≤ 1000`
