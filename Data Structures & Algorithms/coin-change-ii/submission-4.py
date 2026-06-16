class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # idx matters.
        memo = {}
        
        def dfs(idx, total) :
            if (idx, total) in memo :
                return memo[(idx, total)]

            if not total : return 1

            if idx >= len(coins) :
                return 0

            res = 0
            for i in range(idx, len(coins)) :
                if total - coins[i] >= 0 :
                    res += dfs(i, total - coins[i])

            memo[(idx, total)] = res
            return res

        return dfs(0, amount)
