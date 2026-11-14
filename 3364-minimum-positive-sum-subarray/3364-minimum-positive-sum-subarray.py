class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n = len(nums)
        min_sum = float("inf")

        for i in range(n):
            current_sum = 0
            # Only iterate up to the maximum allowed length 'r' or the end of the array
            for j in range(i, min(n, i + r)):
                current_sum += nums[j]
                length = j - i + 1

                if length >= l and current_sum > 0:
                    min_sum = min(min_sum, current_sum)

        return min_sum if min_sum != float("inf") else -1