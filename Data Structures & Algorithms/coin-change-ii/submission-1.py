class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        row = [0] * (amount + 1)
        row[0] = 1

        for i in range(len(coins)-1, -1, -1) :
            for amt in range(coins[i], amount + 1) :
                row[amt] += row[amt - coins[i]]

        return row[amount]