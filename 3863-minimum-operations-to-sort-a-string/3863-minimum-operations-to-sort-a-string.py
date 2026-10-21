class Solution:
    def minOperations(self, s: str) -> int:
       
        sorted_s = "".join(sorted(s))

        # Case 0: Already sorted
        if s == sorted_s:
            return 0

        n = len(s)

        # Impossible: cannot sort entire string of length 2
        if n <= 2:
            return -1

        min_c = sorted_s[0]
        max_c = sorted_s[-1]

        # Case 1: First is min OR last is max
        if s[0] == min_c or s[-1] == max_c:
            return 1

        # Case 3: Needs 3 operations only if min_c is exclusively at the end
        # AND max_c is exclusively at the beginning
        if (
            s[0] == max_c
            and s[-1] == min_c
            and s.count(min_c) == 1
            and s.count(max_c) == 1
        ):
            return 3

        # Case 2: In all other scenarios, 2 operations suffice
        return 2