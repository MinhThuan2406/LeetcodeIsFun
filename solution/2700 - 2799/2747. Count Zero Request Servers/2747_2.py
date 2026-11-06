# 2747. Count Zero Request Servers | Medium
# https://leetcode.com/problems/count-zero-request-servers/
# Array, Hash Table, Sliding Window, Sorting
# Complexity:
# + Time: O(L log L + Q log Q), L = len(logs), Q = len(queries)
# + Space: O(n + Q)

from collections import defaultdict

class Solution:
    def countServers(self, n: int, logs: list[list[int]], x: int, queries: list[int]) -> list[int]:
        logs.sort(key=lambda log: log[1])

        sorted_queries = sorted(enumerate(queries), key=lambda q: q[1])

        ans = [0] * len(queries)
        server_counts = defaultdict(int)
        active_servers = 0
        left = 0
        right = 0
        num_logs = len(logs)

        for original_idx, query_time in sorted_queries:
            window_start = query_time - x
            window_end = query_time

            while right < num_logs and logs[right][1] <= window_end:
                s_id = logs[right][0]
                if server_counts[s_id] == 0:
                    active_servers += 1
                server_counts[s_id] += 1
                right += 1

            while left < num_logs and logs[left][1] < window_start:
                s_id = logs[left][0]
                server_counts[s_id] -= 1
                if server_counts[s_id] == 0:
                    active_servers -= 1
                left += 1

            ans[original_idx] = n - active_servers

        return ans
