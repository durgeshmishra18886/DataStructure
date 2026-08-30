class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return n
        arr=[0,0]
        min1=max1=nums[0]
        for i in range(len(nums)):
            if nums[i] < min1:
                min1=nums[i]
                arr[0]=i
            if nums[i] > max1:
                max1=nums[i]
                arr[1]=i

            low = min(arr[0], arr[1])
            high = max(arr[0], arr[1])
        return min(high + 1, n - low, (low + 1) + (n - high))

        