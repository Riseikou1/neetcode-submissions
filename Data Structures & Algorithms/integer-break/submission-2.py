class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[1] = 1

        for target in range(2, n + 1) :
            dp[target] = target if target != n else 0
            for j in range(1, target) :
                dp[target] = max(dp[target], dp[target - j] * dp[j])

        return dp[n]

