class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyPrice = prices[0]
        res = 0
        for i in range(1,len(prices)):
            if prices[i] < buyPrice :
                buyPrice = prices[i]
            else :
                res = max(res,prices[i]-buyPrice)
        return res