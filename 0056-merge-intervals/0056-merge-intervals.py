class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        
        intervals.sort(key=lambda x: x[0])
        merged=[intervals[0]]

        for current in intervals[1:]:
            prev_low , prev_high= merged[-1]
            curr_low, curr_high=current

            if curr_low <= prev_high:
                merged[-1][1]=max(curr_high,prev_high)
            else: 
                merged.append(current)
        return merged 

