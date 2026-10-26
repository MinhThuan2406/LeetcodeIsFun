# 1462. Course Schedule IV
# Difficulty: Medium

# Floyd-Warshall algorithm
# Runtime: 21ms (27/01/2025 | 11pm - GMT+7)

# Complexity:
# + Time: O(N^3)
# + Space: O(N^2)

from typing import List


class Solution:
    def checkIfPrerequisite(
        self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]
    ) -> List[bool]:
        # Step 1 & 2: Initialize prerequisite matrix
        is_prereq = [[False] * numCourses for _ in range(numCourses)]
        for u, v in prerequisites:
            is_prereq[u][v] = True

        # Step 3: Compute transitive closure using Floyd-Warshall
        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    if is_prereq[i][k] and is_prereq[k][j]:
                        is_prereq[i][j] = True

        # Step 4: Answer each query
        return [is_prereq[u][v] for u, v in queries]
