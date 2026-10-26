class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        divisible_islands = 0

        def dfs(r: int, c: int) -> int:
            if not (0 <= r < m and 0 <= c < n) or grid[r][c] <= 0:
                return 0
            
            # Save cell value and set to 0 to mark visited
            val = grid[r][c]
            grid[r][c] = 0
            
            return val + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)

        for r in range(m):
            for c in range(n):
                if grid[r][c] > 0:
                    total_val = dfs(r, c)
                    if total_val % k == 0:
                        divisible_islands += 1
                        
        return divisible_islands