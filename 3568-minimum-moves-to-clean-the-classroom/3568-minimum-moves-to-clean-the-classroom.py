class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])
    
        start = None
        litters = []
        
        for r in range(m):
            for c in range(n):
                if classroom[r][c] == 'S':
                    start = (r, c)
                elif classroom[r][c] == 'L':
                    litters.append((r, c))
                    
        total_litter = len(litters)
        if total_litter == 0:
            return 0
        
        target_mask = (1 << total_litter) - 1
        litter_map = {pos: i for i, pos in enumerate(litters)}
        
        # max_energy_seen[r][c][mask] stores the highest remaining energy recorded
        max_energy_seen = [[[-1] * (1 << total_litter) for _ in range(n)] for _ in range(m)]
        
        sr, sc = start
        queue = deque([(sr, sc, energy, 0, 0)]) # (r, c, current_energy, mask, moves)
        max_energy_seen[sr][sc][0] = energy
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        while queue:
            r, c, curr_energy, mask, moves = queue.popleft()
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < m and 0 <= nc < n and classroom[nr][nc] != 'X':
                    next_energy = curr_energy - 1
                    if next_energy < 0:
                        continue
                    
                    # Energy reset upon reaching 'R'
                    if classroom[nr][nc] == 'R':
                        next_energy = energy
                    
                    # Check for litter collection
                    next_mask = mask
                    if (nr, nc) in litter_map:
                        next_mask |= (1 << litter_map[(nr, nc)])
                    
                    # If all litter collected
                    if next_mask == target_mask:
                        return moves + 1
                    
                    # Prune paths that have <= energy for the same (cell, mask)
                    if next_energy > max_energy_seen[nr][nc][next_mask]:
                        max_energy_seen[nr][nc][next_mask] = next_energy
                        queue.append((nr, nc, next_energy, next_mask, moves + 1))
                        
        return -1