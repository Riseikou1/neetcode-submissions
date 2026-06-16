class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()
        memo = {}
        def coin_shit(idx, total) :
            if total == 0 :
                return 1

            if (idx, total) in memo :
                return memo[(idx, total)]
            
            if idx >= len(coins) or total < 0 : return 0

            res = 0
            for i in range(idx, len(coins)) :
                if coins[i] > total or total - coins[i] < 0 : break
                res += coin_shit(i, total - coins[i])

            memo[(idx, total)] = res
            return res

        return coin_shit(0, amount)
