class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best=nums[0]
        curr=0
        for n in nums:
            if curr < 0:
                curr=0
            curr+=n
            best=max(best,curr)
        return best

        