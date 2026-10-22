class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0

        is_ascending = True
        is_descending = True

        for i in range(n):
            nxt = (i + 1) % n
            if (nums[i] + 1) % n != nums[nxt]:
                is_ascending = False
            if (nums[i] - 1 + n) % n != nums[nxt]:
                is_descending = False

        if not is_ascending and not is_descending:
            return -1

        k = nums.index(0)

        if is_ascending:
            if k == 0:
                return 0
            # 1. Left rotate k times: cost = k
            # 2. Right rotate (n - k) times using 2 reverses: cost = (n - k) + 2
            return min(k, (n - k) + 2)

        if is_descending:
            # 1. Rotate left (k + 1) % n times, then reverse: cost = (k + 1) % n + 1
            # 2. Reverse first, then rotate left (n - 1 - k) times: cost = 1 + (n - 1 - k)
            cost1 = ((k + 1) % n) + 1
            cost2 = 1 + (n - 1 - k)
            return min(cost1, cost2)