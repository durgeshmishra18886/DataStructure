class Solution:
    def numOfWays(self, nums: list[int]) -> int:
        MOD = 10**9 + 7
        
        def count_ways(arr: list[int]) -> int:
            if len(arr) <= 2:
                return 1
            
            root = arr[0]
            left = [x for x in arr[1:] if x < root]
            right = [x for x in arr[1:] if x > root]
            
            # math.comb(n, k) calculates n! / (k! * (n - k)!)
            ways = math.comb(len(left) + len(right), len(left)) % MOD
            return (ways * count_ways(left) % MOD * count_ways(right)) % MOD
        
        # Subtract 1 to exclude the original array order
        return (count_ways(nums) - 1) % MOD