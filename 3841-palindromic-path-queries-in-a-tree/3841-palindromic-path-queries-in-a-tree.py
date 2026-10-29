class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        LOG = n.bit_length() + 1
        up = [[0] * LOG for _ in range(n)]
        depth = [0] * n
        tin = [0] * n
        tout = [0] * n
        timer = 0

        node_char = list(s)
        dist_xor = [0] * n

        # Iterative DFS for tree traversal, subtree entry/exit times, and binary lifting
        def dfs():
            nonlocal timer
            call_stack = [(0, -1, 0, 1 << (ord(node_char[0]) - ord('a')), 0)]
            while call_stack:
                u, p, d, curr_xor, state = call_stack.pop()
                if state == 0:
                    timer += 1
                    tin[u] = timer
                    depth[u] = d
                    up[u][0] = p if p != -1 else 0
                    dist_xor[u] = curr_xor
                    for i in range(1, LOG):
                        up[u][i] = up[up[u][i - 1]][i - 1]
                    
                    call_stack.append((u, p, d, curr_xor, 1))
                    for v in adj[u]:
                        if v != p:
                            v_xor = curr_xor ^ (1 << (ord(node_char[v]) - ord('a')))
                            call_stack.append((v, u, d + 1, v_xor, 0))
                else:
                    tout[u] = timer

        dfs()

        def get_lca(u: int, v: int) -> int:
            if depth[u] < depth[v]:
                u, v = v, u
            diff = depth[u] - depth[v]
            for i in range(LOG):
                if (diff >> i) & 1:
                    u = up[u][i]
            if u == v:
                return u
            for i in range(LOG - 1, -1, -1):
                if up[u][i] != up[v][i]:
                    u = up[u][i]
                    v = up[v][i]
            return up[u][0]

        # Binary Indexed Tree (Fenwick Tree) for subtree XOR range updates & point queries
        bit = [0] * (n + 2)

        def bit_update(idx: int, val: int):
            while idx <= n + 1:
                bit[idx] ^= val
                idx += idx & (-idx)

        def bit_query(idx: int) -> int:
            res = 0
            while idx > 0:
                res ^= bit[idx]
                idx -= idx & (-idx)
            return res

        def range_xor_update(l: int, r: int, val: int):
            bit_update(l, val)
            bit_update(r + 1, val)

        def get_curr_dist_xor(node: int) -> int:
            return dist_xor[node] ^ bit_query(tin[node])

        ans = []
        for q in queries:
            parts = q.split()
            if parts[0] == "update":
                u = int(parts[1])
                new_c = parts[2]
                old_c = node_char[u]
                if old_c != new_c:
                    delta = (1 << (ord(old_c) - ord('a'))) ^ (1 << (ord(new_c) - ord('a')))
                    node_char[u] = new_c
                    # Subtree of u maps to range [tin[u], tout[u]]
                    range_xor_update(tin[u], tout[u], delta)
            else:
                u = int(parts[1])
                v = int(parts[2])
                lca = get_lca(u, v)
                lca_mask = 1 << (ord(node_char[lca]) - ord('a'))
                
                # Path parity mask: dist(u) ^ dist(v) ^ mask(lca)
                path_mask = get_curr_dist_xor(u) ^ get_curr_dist_xor(v) ^ lca_mask
                
                # A set of characters can form a palindrome iff at most one character has an odd frequency
                can_palindrome = (path_mask & (path_mask - 1)) == 0
                ans.append(can_palindrome)

        return ans