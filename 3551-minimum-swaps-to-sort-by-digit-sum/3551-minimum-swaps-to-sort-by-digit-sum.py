class Solution:

  def minSwaps(self, nums: List[int]) -> int:
    def digit_sum(x: int) -> int:
      s = 0
      while x > 0:
        s += x % 10
        x //= 10
      return s

    n = len(nums)

    # 1. Determine the sorted target order based on (digit_sum, value)
    sorted_nums = sorted(nums, key=lambda x: (digit_sum(x), x))

    # 2. Map each number to its target index in the sorted array
    target_idx = {val: i for i, val in enumerate(sorted_nums)}

    # 3. Cycle decomposition to count the minimum swaps
    visited = [False] * n
    swaps = 0

    for i in range(n):
      # Skip if already visited or already in the correct position
      if visited[i] or target_idx[nums[i]] == i:
        continue

      cycle_size = 0
      curr = i
      while not visited[curr]:
        visited[curr] = True
        curr = target_idx[nums[curr]]
        cycle_size += 1

      if cycle_size > 1:
        swaps += cycle_size - 1

    return swaps