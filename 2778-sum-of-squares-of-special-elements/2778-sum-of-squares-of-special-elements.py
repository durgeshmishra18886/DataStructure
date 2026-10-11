class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        len_arr= len(nums)
        sum=0
        for i in range(1,len_arr+1):
            
            if len_arr % (i) == 0 :
                sum += nums[i-1] * nums[i-1] 
        return sum


        