class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        ans = [0] * k
        # dp[r] will store the number of subarrays ending at the current index
        # whose product modulo k is equal to r.
        dp = [0] * k
        
        for val in nums:
            val_mod = val % k
            new_dp = [0] * k
            
            # Transition from previous subarrays
            for r in range(k):
                if dp[r] > 0:
                    new_r = (r * val_mod) % k
                    new_dp[new_r] += dp[r]
            
            # The single-element subarray [val]
            new_dp[val_mod] += 1
            
            # Add all subarrays ending at the current index to the total counts
            for r in range(k):
                ans[r] += new_dp[r]
                
            dp = new_dp
            
        return ans