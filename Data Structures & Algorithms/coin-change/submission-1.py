class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def dfs(total) :
            if total == 0 :
                return 0
            if total in memo :
                return memo[total]
            
            res = 1e9
            for coin in coins :
                if total - coin >= 0 :
                    res = min(res, 1 + dfs(total - coin))

            memo[total] = res
            return res  

        res = dfs(amount)
        return res if res != 1e9 else -1
