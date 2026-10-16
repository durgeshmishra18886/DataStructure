class SegmentTree:
    def __init__(self, n: int, mod: int = 1_000_000_007):
        self.n = n
        self.mod = mod
        self.sum_sq = [0] * (4 * n)
        self.sum_val = [0] * (4 * n)
        self.lazy = [0] * (4 * n)

    def _apply(self, node: int, v: int, length: int):
        # (x + v)^2 = x^2 + 2vx + v^2
        self.sum_sq[node] = (
            self.sum_sq[node]
            + 2 * v * self.sum_val[node]
            + v * v * length
        ) % self.mod
        self.sum_val[node] = (self.sum_val[node] + v * length) % self.mod
        self.lazy[node] = (self.lazy[node] + v) % self.mod

    def _push(self, node: int, left: int, right: int):
        if self.lazy[node] != 0:
            mid = (left + right) // 2
            self._apply(2 * node, self.lazy[node], mid - left + 1)
            self._apply(2 * node + 1, self.lazy[node], right - mid)
            self.lazy[node] = 0

    def update(self, ql: int, qr: int, v: int, node: int, l: int, r: int):
        if ql <= l and r <= qr:
            self._apply(node, v, r - l + 1)
            return

        self._push(node, l, r)
        mid = (l + r) // 2
        if ql <= mid:
            self.update(ql, qr, v, 2 * node, l, mid)
        if qr > mid:
            self.update(ql, qr, v, 2 * node + 1, mid + 1, r)

        self.sum_sq[node] = (self.sum_sq[2 * node] + self.sum_sq[2 * node + 1]) % self.mod
        self.sum_val[node] = (self.sum_val[2 * node] + self.sum_val[2 * node + 1]) % self.mod


class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        MOD = 1_000_000_007
        n = len(nums)
        tree = SegmentTree(n, MOD)
        last_pos = {}
        ans = 0

        for j, val in enumerate(nums):
            prev = last_pos.get(val, -1)
            # Add 1 to distinct counts for all subarrays starting in [prev + 1, j]
            tree.update(prev + 1, j, 1, 1, 0, n - 1)
            last_pos[val] = j
            
            # tree.sum_sq[1] holds the sum of squares for all subarrays ending at index j
            ans = (ans + tree.sum_sq[1]) % MOD

        return ans
        