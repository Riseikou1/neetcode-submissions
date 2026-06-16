class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}

        def dfs(i, total) :
            if total == 0 : return 1

            if total < 0 or i >= len(coins) :
                return 0

            if (i, total) in memo :
                return memo[(i, total)]

            res = dfs(i + 1, total) + dfs(i, total - coins[i])

            memo[(i, total)] = res
            return res

        return dfs(0, amount)