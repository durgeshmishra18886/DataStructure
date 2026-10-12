class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        bit_counts = [0] * 32
        
        # Count the total number of 1s at each bit position
        for num in nums:
            for i in range(32):
                if (num >> i) & 1:
                    bit_counts[i] += 1
        
        ans = 0
        # Form the k largest possible numbers
        for _ in range(k):
            current_num = 0
            for i in range(32):
                if bit_counts[i] > 0:
                    current_num |= (1 << i)
                    bit_counts[i] -= 1
            
            ans = (ans + current_num * current_num) % MOD
            
        return ans