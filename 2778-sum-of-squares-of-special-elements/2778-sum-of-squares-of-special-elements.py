class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n= len(nums)
        sum=0
        for i in range(1,n+1):
                if n % i == 0 :
                    sum += nums[i-1] * nums[i-1] 
        return sum


        