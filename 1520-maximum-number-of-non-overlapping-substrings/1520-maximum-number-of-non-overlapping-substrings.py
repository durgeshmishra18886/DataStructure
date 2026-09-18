class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        # Step 1: Record first and last occurrences of each character
        first = {}
        last = {}
        for i, ch in enumerate(s):
            if ch not in first:
                first[ch] = i
            last[ch] = i

        # Step 2: Find all valid candidate intervals [i, r]
        intervals = []
        for ch in first:
            i = first[ch]
            r = last[ch]
            valid = True
            
            j = i
            while j <= r:
                c = s[j]
                # If a character appeared before our chosen start 'i',
                # an interval starting at 'i' cannot be valid.
                if first[c] < i:
                    valid = False
                    break
                r = max(r, last[c])
                j += 1
                
            if valid:
                intervals.append((i, r))

        # Step 3: Sort candidate intervals by their end index (Greedy Interval Scheduling)
        intervals.sort(key=lambda x: x[1])

        # Step 4: Pick non-overlapping intervals
        res = []
        prev_end = -1
        for start, end in intervals:
            if start > prev_end:
                res.append(s[start : end + 1])
                prev_end = end

        return res
        