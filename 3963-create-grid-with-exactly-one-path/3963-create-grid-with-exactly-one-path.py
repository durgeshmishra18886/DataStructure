class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        grid = [["#" for _ in range(n)] for _ in range(m)]

        for c in range(n):
            grid[0][c] = "."

        for r in range(m):
            grid[r][n - 1] = "."

       
        return ["".join(row) for row in grid]