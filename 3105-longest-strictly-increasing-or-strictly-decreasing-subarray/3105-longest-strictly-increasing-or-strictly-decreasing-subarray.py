class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        max_len = 1
        inc_len = 1  # Length of current strictly increasing window
        dec_len = 1  # Length of current strictly decreasing window
        
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                inc_len += 1
                dec_len = 1  # Reset decreasing window
            elif nums[i] < nums[i - 1]:
                dec_len += 1
                inc_len = 1  # Reset increasing window
            else:
                # Equal elements break both strictly increasing and decreasing
                inc_len = 1
                dec_len = 1
                
            max_len = max(max_len, inc_len, dec_len)
            
        return max_len