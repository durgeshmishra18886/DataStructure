class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        
        # A valid parentheses string must have an even length
        total_len = m + n - 1
        if total_len % 2 != 0:
            return False
        
        # Must start with '(' and end with ')'
        if grid[0][0] == ')' or grid[m - 1][n - 1] == '(':
            return False
        
        # Max open parentheses allowed in any valid string of length total_len
        max_open = total_len // 2
        
        # visited will store (row, col, balance)
        visited = set()
        visited.add((0, 0, 1))
        
        # Queue/list of active states for BFS
        current_layer = {(0, 0, 1)}
        
        while current_layer:
            next_layer = set()
            
            for r, c, bal in current_layer:
                if r == m - 1 and c == n - 1:
                    if bal == 0:
                        return True
                    continue
                
                # Check moving right and moving down
                for nr, nc in ((r, c + 1), (r + 1, c)):
                    if nr < m and nc < n:
                        nbal = bal + (1 if grid[nr][nc] == '(' else -1)
                        
                        # Pruning:
                        # 1. nbal cannot drop below 0
                        # 2. nbal cannot exceed max_open
                        # 3. nbal cannot exceed the remaining steps left to reach (m-1, n-1)
                        remaining_steps = (m - 1 - nr) + (n - 1 - nc)
                        if 0 <= nbal <= remaining_steps and nbal <= max_open:
                            state = (nr, nc, nbal)
                            if state not in visited:
                                visited.add(state)
                                next_layer.add(state)
                                
            current_layer = next_layer
            
        return False