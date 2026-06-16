class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        l = 0

        for r in range(1, len(prices)) :
            if prices[r] > prices[l] :
                res += prices[r] - prices[l]
            l = r

        return res
