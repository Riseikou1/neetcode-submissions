class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        dp = [0] * (n + 1)
        dp[n] = 1  # empty t

        for i in range(m - 1, -1, -1):
            diag = dp[n]  # this is dp[i+1][n] == 1
            for j in range(n - 1, -1, -1):
                tmp = dp[j]          # save dp[i+1][j]
                if s[i] == t[j]:
                    dp[j] = dp[j] + diag  # dp[i+1][j] + dp[i+1][j+1]
                    
                # else dp[j] stays dp[i+1][j]
                diag = tmp           # move diagonal for next j
                
        return dp[0]
