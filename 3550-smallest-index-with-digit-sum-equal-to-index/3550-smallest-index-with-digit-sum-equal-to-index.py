class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i,val in enumerate(nums):
            curr=val
            sum=0
            if curr > 9: 
                while curr >  0:
                    rem=curr % 10
                    curr= curr // 10
                    sum+=rem
            else:
                sum = val
            if i == sum:
                return i
        return -1