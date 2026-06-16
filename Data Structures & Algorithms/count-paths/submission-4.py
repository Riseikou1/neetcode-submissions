class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        rows, cols = m, n
        dp = [1] * cols

        for r in range(1, rows) :
            for c in range(1, cols) :
                dp[c] += dp[c - 1]

        return dp[cols - 1]
