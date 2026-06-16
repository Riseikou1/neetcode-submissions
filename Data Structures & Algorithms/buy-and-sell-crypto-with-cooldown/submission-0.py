class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {} 

        def dfs(i, buying) :
            if i >= len(prices) :
                return 0

            if (i, buying) in memo : 
                return memo[(i, buying)]

            if buying :  # decide to buy or skip.
                skip = dfs(i + 1, buying)
                buy = dfs(i + 1, not buying) - prices[i]
                memo[(i, buying)] = max(skip, buy)

            else :   # decide to sell or skip.
                skip = dfs(i + 1, buying)
                sell = dfs(i + 2, not buying) + prices[i] # if you sell the shit, there is a cooldown.
                memo[(i, buying)] = max(skip, sell)
        
            return memo[(i, buying)]
        return dfs(0, True)
