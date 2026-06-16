class Solution:
    def uniquePathsWithObstacles(self, grid : List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dp = [0] * (cols + 1)
        dp[cols - 1] = 1

        for r in range(rows-1, -1, -1) :
            for c in range(cols -1, -1, -1) :
                if grid[r][c] == 1 :
                    dp[c] = 0
                else :
                    dp[c] += dp[c + 1]

        return dp[0]