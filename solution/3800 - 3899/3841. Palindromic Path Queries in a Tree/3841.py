# 3841. Palindromic Path Queries in a Tree | Hard
# https://leetcode.com/problems/palindromic-path-queries-in-a-tree/
# Binary Lifting + XOR BIT
# Complexity:
# + Time: O((n + q) log n), n = number of nodes, q = number of queries
# + Space: O(n log n)

class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        LOG = max(1, n.bit_length())
        tin = [0] * n
        tout = [0] * n
        up = [[-1] * LOG for _ in range(n)]

        timer = 0
        stack = [(0, -1)]
        while stack:
            u, p = stack.pop()
            if u >= 0:
                timer += 1
                tin[u] = timer
                up[u][0] = p
                for i in range(1, LOG):
                    mid = up[u][i - 1]
                    if mid != -1:
                        up[u][i] = up[mid][i - 1]
                stack.append((~u, p))
                for v in adj[u]:
                    if v != p:
                        stack.append((v, u))
            else:
                tout[~u] = timer

        def is_ancestor(u: int, v: int) -> bool:
            return tin[u] <= tin[v] and tout[v] <= tout[u]

        def get_lca(u: int, v: int) -> int:
            if is_ancestor(u, v):
                return u
            if is_ancestor(v, u):
                return v
            for i in range(LOG - 1, -1, -1):
                a = up[u][i]
                if a != -1 and not is_ancestor(a, v):
                    u = a
            return up[u][0]

        # XOR BIT: range-xor update, point query (root-to-node prefix mask)
        bit = [0] * (n + 2)

        def bit_update(i: int, val: int) -> None:
            while i <= n + 1:
                bit[i] ^= val
                i += i & -i

        def bit_query(i: int) -> int:
            res = 0
            while i > 0:
                res ^= bit[i]
                i -= i & -i
            return res

        def subtree_xor(u: int, val: int) -> None:
            bit_update(tin[u], val)
            bit_update(tout[u] + 1, val)

        cur = list(s)
        for i in range(n):
            subtree_xor(i, 1 << (ord(cur[i]) - ord('a')))

        ans = []
        for q in queries:
            parts = q.split()
            if parts[0] == "update":
                u, c = int(parts[1]), parts[2]
                diff = (1 << (ord(cur[u]) - ord('a'))) ^ (1 << (ord(c) - ord('a')))
                if diff:
                    subtree_xor(u, diff)
                    cur[u] = c
            else:
                u, v = int(parts[1]), int(parts[2])
                lca = get_lca(u, v)
                mask = bit_query(tin[u]) ^ bit_query(tin[v]) ^ (1 << (ord(cur[lca]) - ord('a')))
                ans.append((mask & (mask - 1)) == 0)
        return ans
