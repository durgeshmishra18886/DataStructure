class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        n = len(arr)
        # prefix_map stores: prefix_sum -> latest_index
        prefix_map = {0: -1}
        
        # min_len[i] stores the minimum length of a valid subarray ending at or before index i
        min_len = [float('inf')] * n
        
        curr_sum = 0
        min_sum_len = float('inf')
        
        for i in range(n):
            curr_sum += arr[i]
            
            # Check if there is a subarray ending at i with sum equal to target
            if (curr_sum - target) in prefix_map:
                prev_idx = prefix_map[curr_sum - target]
                curr_len = i - prev_idx
                
                # If a valid subarray exists before prev_idx, update the answer
                if prev_idx >= 0 and min_len[prev_idx] != float('inf'):
                    min_sum_len = min(min_sum_len, curr_len + min_len[prev_idx])
                
                # Update min_len[i] with the current subarray length
                if i > 0:
                    min_len[i] = min(min_len[i - 1], curr_len)
                else:
                    min_len[i] = curr_len
            else:
                # Carry forward the previous minimum length
                if i > 0:
                    min_len[i] = min_len[i - 1]
                    
            prefix_map[curr_sum] = i

        return min_sum_len if min_sum_len != float('inf') else -1