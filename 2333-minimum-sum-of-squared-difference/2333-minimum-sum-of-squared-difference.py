class Solution:

  def minSumSquareDiff(
      self, nums1: list[int], nums2: list[int], k1: int, k2: int
  ) -> int:
    k = k1 + k2
    diffs = [abs(a - b) for a, b in zip(nums1, nums2)]

    total_diff = sum(diffs)
    if total_diff <= k:
      return 0

    max_val = max(diffs)
    count = [0] * (max_val + 1)
    for d in diffs:
      count[d] += 1

    # Greedily reduce from the highest difference
    for v in range(max_val, 0, -1):
      if count[v] == 0:
        continue

      if k >= count[v]:
        k -= count[v]
        count[v - 1] += count[v]
        count[v] = 0
      else:
        count[v - 1] += k
        count[v] -= k
        k = 0
        break

    return sum(v * v * cnt for v, cnt in enumerate(count))