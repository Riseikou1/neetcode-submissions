class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse = True)
        self.res = float('inf')
        def dfs(idx ,total, depth) :
            if total == 0 : 
                self.res = min(self.res, depth) 
                return 
            if idx >= len(coins) :
                return 

            max_use = total // coins[idx]
            for k in range(max_use, -1, -1) :
                if depth + max_use >= self.res :
                    break

                dfs(idx + 1, total - k * coins[idx], depth + k)

        dfs(0, amount, 0)
        return self.res if self.res != float('inf') else -1