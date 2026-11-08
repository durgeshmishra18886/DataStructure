class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        row_count = [0] * m
        col_count = [0] * n
        
        # Step 1: Count servers in each row and each column
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    row_count[r] += 1
                    col_count[c] += 1
                    
        # Step 2: Count servers that share their row or column with another server
        communicating_servers = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    if row_count[r] > 1 or col_count[c] > 1:
                        communicating_servers += 1
                        
        return communicating_servers