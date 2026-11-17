class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        INF = float('inf')

        # 1. Precompute proper divisors for all possible substring lengths (2 to n)
        divisors = [[] for _ in range(n + 1)]
        for length in range(2, n + 1):
            for d in range(1, length):
                if length % d == 0:
                    divisors[length].append(d)

        # Helper to compute min changes to make s[i..j] a semi-palindrome
        def get_cost(i: int, j: int) -> int:
            length = j - i + 1
            min_changes = INF
            
            for d in divisors[length]:
                changes = 0
                # Check each of the d interleaved groups
                for start in range(d):
                    left = i + start
                    # Last element in this group within s[i..j]
                    right = j - ((length - 1 - start) % d)
                    while left < right:
                        if s[left] != s[right]:
                            changes += 1
                        left += d
                        right -= d
                if changes < min_changes:
                    min_changes = changes
                    
            return min_changes

        # 2. Precompute cost[i][j] for all valid substrings s[i..j] (length >= 2)
        cost = [[INF] * n for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                cost[i][j] = get_cost(i, j)

        # 3. DP: dp[i][p] = min changes to split s[:i] into p semi-palindromes
        dp = [[INF] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 0

        for p in range(1, k + 1):
            # Each partition needs length >= 2, so i >= 2 * p
            for i in range(2 * p, n + 1):
                # m is the start index of the p-th substring s[m..i-1]
                for m in range(2 * (p - 1), i - 1):
                    if dp[m][p - 1] != INF:
                        dp[i][p] = min(dp[i][p], dp[m][p - 1] + cost[m][i - 1])

        return dp[n][k]