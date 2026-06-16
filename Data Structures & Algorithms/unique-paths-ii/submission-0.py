class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        memo = {(rows - 1, cols - 1) : 1}

        def dfs(r, c) :
            if r >= rows or c >= cols or grid[r][c] == 1 :
                return 0

            if (r, c) in memo :
                return memo[(r, c)]

            memo[(r, c)] = dfs(r + 1, c) + dfs(r, c + 1)
            return memo[(r, c)]

        return dfs(0, 0)