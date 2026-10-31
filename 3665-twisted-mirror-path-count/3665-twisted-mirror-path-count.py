from typing import List

class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])
        
        # Edge case: already at the destination
        if m == 1 and n == 1:
            return 1 if grid[0][0] == 0 else 0
        
        # If the start or destination is blocked/mirror (if applicable)
        if grid[0][0] == 1 or grid[m - 1][n - 1] == 1:
            return 0
        
        # right[i][j]: ways to enter (i, j) moving Right
        # down[i][j]: ways to enter (i, j) moving Down
        right = [[0] * n for _ in range(m)]
        down = [[0] * n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    if j + 1 < n:
                        right[0][1] = 1
                    if i + 1 < m:
                        down[1][0] = 1
                    continue
                
                if grid[i][j] == 0:
                    # Empty cell: robot lands here and can choose either Right or Down
                    total_ways = (right[i][j] + down[i][j]) % MOD
                    if j + 1 < n:
                        right[i][j + 1] = (right[i][j + 1] + total_ways) % MOD
                    if i + 1 < m:
                        down[i + 1][j] = (down[i + 1][j] + total_ways) % MOD
                else:
                    # Mirror cell:
                    # 1. Entered moving Right -> reflected Down to (i + 1, j)
                    if i + 1 < m:
                        down[i + 1][j] = (down[i + 1][j] + right[i][j]) % MOD
                    # 2. Entered moving Down -> reflected Right to (i, j + 1)
                    if j + 1 < n:
                        right[i][j + 1] = (right[i][j + 1] + down[i][j]) % MOD
                        
        # Total ways to reach the destination (m - 1, n - 1) from either direction
        return (right[m - 1][n - 1] + down[m - 1][n - 1]) % MOD