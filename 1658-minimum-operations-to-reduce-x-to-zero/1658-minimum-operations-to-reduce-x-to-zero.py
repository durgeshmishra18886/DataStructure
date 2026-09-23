class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        target = sum(nums) - x
    
        # Edge case 1: We need exactly all elements in the array
        if target == 0:
            return len(nums)
            
        # Edge case 2: The sum of all elements is less than x
        if target < 0:
            return -1
            
        max_window_len = -1
        current_sum = 0
        left = 0
        
        # Sliding window execution
        for right in range(len(nums)):
            current_sum += nums[right]
            
            # If our window's sum is too large, shrink it from the left
            while current_sum > target and left <= right:
                current_sum -= nums[left]
                left += 1
                
            # If we hit the exact target, update our max window length
            if current_sum == target:
                max_window_len = max(max_window_len, right - left + 1)
                
        # If we never found a valid window, return -1
        if max_window_len == -1:
            return -1
            
        # The answer is the total elements minus the elements we kept in the middle
        return len(nums) - max_window_len 