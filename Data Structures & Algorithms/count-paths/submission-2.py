class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        rows, cols = m, n
        dp = [[0] * (cols + 1) for _ in range(rows + 1)]
        dp[rows][cols - 1] = 1

        for r in range(rows - 1, -1, -1) :
            for c in range(cols - 1, -1, -1) :
                dp[r][c] += dp[r + 1][c] + dp[r][c + 1]

        return dp[0][0]
