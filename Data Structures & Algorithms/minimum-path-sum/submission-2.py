class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        memo = {(rows - 1, cols - 1) : grid[rows - 1][cols - 1]}

        def dfs(r, c) :
            if (r, c) in memo :
                return memo[(r, c)]

            if r not in range(rows) or c not in range(cols) : return float('inf')

            res = min(dfs(r + 1, c) + grid[r][c],  dfs(r, c + 1) + grid[r][c]) 

            memo[(r, c)] = res
            return res

        return dfs(0, 0)

