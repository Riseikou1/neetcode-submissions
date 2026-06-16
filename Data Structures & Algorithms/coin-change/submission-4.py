class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def dfs(i, total) :
            if (i, total) in memo : 
                return memo[(i, total)]

            if total == 0 : return 0

            if i >= len(coins) or total < 0 : return float('inf')

            take = 1 + dfs(i, total - coins[i])
            skip = dfs(i + 1, total)

            memo[(i, total)] = min(take, skip)
            return memo[(i, total)]

        res = dfs(0, amount)
        return res if res != float('inf') else -1