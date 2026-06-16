import math
class Solution:
    def numSquares(self, n: int) -> int:
        memo = {0 : 0}
        def dfs(total) :
            if total in memo :
                return memo[total]
            
            res = total
            for i in range(1, total + 1) :
                if i ** 2 > total : break
                res = min(res, 1 + dfs(total - i ** 2))
            memo[total] = res
            return res

        return dfs(n)
    
