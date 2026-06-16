class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        dp = [0] * n

        for l in range(n - 1, -1, -1) :
            for r in range(l, n) :
                even = (r - l) % 2 == 0
                left = piles[l] if even else 0
                right = piles[r] if even else 0
                if l == r :
                    dp[r] = left
                else :
                    dp[r] = max(left + dp[r], right + dp[r - 1])

        return dp[n - 1] > sum(piles) // 2