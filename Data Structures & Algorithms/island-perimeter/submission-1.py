class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()

        def dfs(r, c) :
            if (r not in range(rows) or c not in range(cols)
                or grid[r][c] == 0) :
                return 1

            if (r, c) in visited : return 0

            visited.add((r, c))
            res = dfs(r + 1,c) + dfs(r,c + 1)+ dfs(r - 1,c) + dfs(r,c - 1)

            return res
        
        for r in range(rows) :
            for c in range(cols) :
                if grid[r][c] :
                    return dfs(r, c)

        return 0

