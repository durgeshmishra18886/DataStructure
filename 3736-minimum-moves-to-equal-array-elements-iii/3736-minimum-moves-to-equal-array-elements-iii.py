class Solution:
    def minMoves(self, nums: List[int]) -> int:
        maxima=max(nums)
        sum=0
        for i in nums:
            sum+=maxima - i
        return sum
        