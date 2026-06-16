class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # dp1_buy = buy [i + 1]    buy it next day.
        # dp_1 sell = sell [i + 1] sell it next day.
        # dp_2 buy = buy [i + 2]   buy it 2 days later (need to use for cooldown time after selling a stock)

        n = len(prices)
        dp2_buy, dp1_buy, dp1_sell = 0, 0, 0

        for i in range(n - 1, -1, -1) :
            dp_buy = max(dp1_sell - prices[i], dp1_buy) # skip or buy today and sell it tmr.
            dp_sell = max(dp2_buy + prices[i], dp1_sell) # skip or sell now and buy 2 days later.

            dp2_buy = dp1_buy
            dp1_buy = dp_buy
            dp1_sell = dp_sell

        return dp1_buy


# simply lovely.

# dp_buy holds the value of maximum between skipping for today, selling tmr.
# and the good thing is selling tmr holds max between 
#     selling tmr and skipping tmr. so on and soo on...
#     so, recursively, we can find the maximum amount shit ..
