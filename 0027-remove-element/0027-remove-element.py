class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left = 0
        right = len(nums) - 1
    
        while left <= right:
            if nums[left] == val:
                # Replace current element with the last valid element
                nums[left] = nums[right]
                right -= 1
            else:
                left += 1
            
        return left