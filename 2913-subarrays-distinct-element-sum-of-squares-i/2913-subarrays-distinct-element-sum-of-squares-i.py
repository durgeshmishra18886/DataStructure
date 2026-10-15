class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        total_sum = 0
        n = len(nums)
        
        # i marks the start of the subarray
        for i in range(n):
            seen = set()
            # j marks the end of the subarray
            for j in range(i, n):
                seen.add(nums[j])
                # len(seen) is the number of distinct elements in nums[i..j]
                distinct_count = len(seen)
                total_sum += distinct_count * distinct_count
                
        return total_sum

     