class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        def dfs(r, c) :
            if not(r in range(rows) and c in range(cols)) or grid[r][c] == '0':
                return 

            grid[r][c] = '0'

            for nr, nc in directions :
                tem_r, tem_c = r + nr, c + nc
                if tem_r in range(rows) and tem_c in range(cols) and grid[tem_r][tem_c] == '1':
                    dfs(tem_r, tem_c) 
        
        rows, cols = len(grid), len(grid[0])
        count = 0

        for i in range(rows) :
            for j in range(cols) :
                if grid[i][j] == '1' :
                    dfs(i, j)
                    count += 1
        
        return count
