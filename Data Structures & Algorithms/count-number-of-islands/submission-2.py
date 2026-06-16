class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(0, 1), (1, 0), (-1, 0), (1, 0)]

        def dfs(r, c) :
            if not(r in range(rows) and c in range(cols)) or grid[r][c] == '0':
                return 

            grid[r][c] = '0'

            dfs(r, c + 1)
            dfs(r, c - 1)
            dfs(r - 1, c)
            dfs(r + 1, c)

        rows, cols = len(grid), len(grid[0])
        count = 0

        for i in range(rows) :
            for j in range(cols) :
                if grid[i][j] == '1' :
                    dfs(i, j)
                    count += 1
        
        return count
