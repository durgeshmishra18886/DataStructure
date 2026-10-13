class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:

        nums.sort(key=abs)
        n= len(nums)//2
        sum_small = [x * x for x in nums[:n]]
        sum_max = [num * num for num in nums[n:]]
        return  sum(sum_max) -  sum(sum_small)

            
        