class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        rows, cols = m, n
        dp = [1] * cols

        for r in range(rows - 2, -1, -1) :
            new_dp = [0] * cols
            new_dp[cols - 1] = 1
            for c in range(cols - 2, -1, -1) :
                new_dp[c] += dp[c] + new_dp[c + 1]
            dp = new_dp
        
        return dp[0]
