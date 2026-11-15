class Solution:

    def numOfSubarrays(self, arr: list[int]) -> int:
        MOD = 10**9 + 7
        
        running_total = 0
        even_count = 1  
        odd_count = 0
        answer = 0
        
        for num in arr:
            running_total += num
            
            if running_total % 2 == 1:  # Current total is odd
                answer += even_count
                odd_count += 1
            else:                       # Current total is even
                answer += odd_count
                even_count += 1
                
        return answer % MOD
            