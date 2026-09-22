class Node:
    def __init__(self, k: int):
        self.prod = 1
        # remain[r] tracks the count of prefixes within this range 
        # that yield a product remainder of 'r' modulo k
        self.remain = [0] * k

class SegmentTree:
    def __init__(self, nums: List[int], k: int):
        self.n = len(nums)
        self.k = k
        self.tree = [Node(k) for _ in range(4 * self.n)]
        self._build(nums, 1, 0, self.n - 1)

    def _merge(self, left: Node, right: Node) -> Node:
        res = Node(self.k)
        res.prod = (left.prod * right.prod) % self.k
        
        # Left child prefix paths are unaffected by prior segments
        for r in range(self.k):
            res.remain[r] += left.remain[r]
            
        # Right child prefix paths are scaled forward by the entire left segment product
        left_prod = left.prod
        for r in range(self.k):
            new_rem = (left_prod * r) % self.k
            res.remain[new_rem] += right.remain[r]
            
        return res

    def _build(self, nums: List[int], node: int, start: int, end: int):
        if start == end:
            val = nums[start] % self.k
            self.tree[node].prod = val
            self.tree[node].remain[val] = 1
            return
        
        mid = (start + end) // 2
        self._build(nums, 2 * node, start, mid)
        self._build(nums, 2 * node + 1, mid + 1, end)
        self.tree[node] = self._merge(self.tree[2 * node], self.tree[2 * node + 1])

    def update(self, node: int, start: int, end: int, idx: int, val: int):
        if start == end:
            self.tree[node].remain = [0] * self.k
            v = val % self.k
            self.tree[node].prod = v
            self.tree[node].remain[v] = 1
            return
        
        mid = (start + end) // 2
        if idx <= mid:
            self.update(2 * node, start, mid, idx, val)
        else:
            self.update(2 * node + 1, mid + 1, end, idx, val)
        self.tree[node] = self._merge(self.tree[2 * node], self.tree[2 * node + 1])

    def query(self, node: int, start: int, end: int, l: int, r: int) -> Node:
        if l <= start and end <= r:
            return self.tree[node]
        
        mid = (start + end) // 2
        if r <= mid:
            return self.query(2 * node, start, mid, l, r)
        if l > mid:
            return self.query(2 * node + 1, mid + 1, end, l, r)
            
        left_res = self.query(2 * node, start, mid, l, mid)
        right_res = self.query(2 * node + 1, mid + 1, end, mid + 1, r)
        return self._merge(left_res, right_res)
        
class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        n = len(nums)
        tree = SegmentTree(nums, k)
        ans = []
        
        for index, value, start, xi in queries:
            # 1. Update nums[index] to value (persistent)
            tree.update(1, 0, n - 1, index, value)
            
            # 2. Query range starting from 'start' to the end of the array (n - 1)
            res_node = tree.query(1, 0, n - 1, start, n - 1)
            
            # 3. Retrieve the count of valid operations for remainder 'xi'
            ans.append(res_node.remain[xi])
            
        return ans