# 2747. Count Zero Request Servers | Medium
# https://leetcode.com/problems/count-zero-request-servers/
# Array, Hash Table, Sliding Window, Sorting
# Complexity:
# + Time: O(L log L + Q log Q), L = len(logs), Q = len(queries)
# + Space: O(n + Q)

from operator import itemgetter

class Solution:
    def countServers(self, n: int, logs: list[list[int]], x: int, queries: list[int]) -> list[int]:
        logs.sort(key=itemgetter(1))
        order = sorted(range(len(queries)), key=queries.__getitem__)

        cnt = [0] * (n + 1)
        active = 0
        left = right = 0
        num_logs = len(logs)
        ans = [0] * len(queries)

        for i in order:
            end = queries[i]
            start = end - x

            while right < num_logs and logs[right][1] <= end:
                s = logs[right][0]
                if cnt[s] == 0:
                    active += 1
                cnt[s] += 1
                right += 1

            while left < right and logs[left][1] < start:
                s = logs[left][0]
                cnt[s] -= 1
                if cnt[s] == 0:
                    active -= 1
                left += 1

            ans[i] = n - active

        return ans
