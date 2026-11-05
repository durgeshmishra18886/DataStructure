class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        count = 0
        for i in arr1:
            is_valid = True
            for j in arr2:
                if abs(i - j) <= d:  # Found an element too close!
                    is_valid = False
                    break
            
            if is_valid:  # Survived all checks
                count += 1
                
        return count

