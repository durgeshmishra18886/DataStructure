class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        c = [0] + costs
    
        dp = [float('inf')] * (n + 1)
        dp[0] = 0  
        
        for i in range(1, n + 1):
            
            for prev in [i - 1, i - 2, i - 3]:
                if prev >= 0:
                    cost = dp[prev] + c[i] + (i - prev) ** 2
                    dp[i] = min(dp[i], cost)
                    
        return dp[n]