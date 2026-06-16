class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        if grid[0][0] == 1 or grid[rows- 1][cols- 1] == 1 :
            return 0
        dp = [[0] * (cols + 1) for _ in range(rows + 1)]
        dp[rows - 1][cols - 1] = 1

        for r in range(rows - 1, -1, -1) :
            for c in range(cols - 1, -1, -1) :
                if not grid[r][c] == 1 :
                    dp[r][c] += dp[r + 1][c] + dp[r][c + 1]

        return dp[0][0]
