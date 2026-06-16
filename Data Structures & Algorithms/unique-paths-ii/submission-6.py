class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        if grid[0][0] == 1 or grid[rows - 1][cols - 1] == 1 : return 0
        memo = {(rows - 1, cols - 1) : 1}

        def dfs(r, c) :
            if (r, c) in memo : return memo[(r, c)]

            if r not in range(rows) or c not in range(cols) or grid[r][c] == 1 :
                 return 0

            res = dfs(r + 1, c) + dfs(r, c + 1)
            memo[(r, c)] = res
            return res

        return dfs(0, 0)

