class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        indexed_intervals = [
            (intervals[i][0], intervals[i][1], intervals[i][2], i)
            for i in range(n)
        ]
        
        # Sort by start coordinate 'l'
        indexed_intervals.sort()
        start_coords = [iv[0] for iv in indexed_intervals]

        @lru_cache(None)
        def dp(i: int, count: int):
            # Base cases: out of intervals or quota reached
            if i >= n or count == 0:
                return (0, ())

            # Option 1: Skip the current interval
            best_weight, best_indices = dp(i + 1, count)

            # Option 2: Take the current interval
            l, r, weight, orig_idx = indexed_intervals[i]
            
            # Find the next interval that does not overlap (l_next > r)
            nxt_idx = bisect_right(start_coords, r)
            next_weight, next_indices = dp(nxt_idx, count - 1)
            
            take_weight = weight + next_weight
            take_indices = tuple(sorted(next_indices + (orig_idx,)))

            # Compare and choose the best option
            if take_weight > best_weight:
                best_weight, best_indices = take_weight, take_indices
            elif take_weight == best_weight:
                if take_indices < best_indices:
                    best_indices = take_indices

            return (best_weight, best_indices)

        # We can pick up to 4 intervals starting from index 0
        _, chosen_indices = dp(0, 4)
        return list(chosen_indices)