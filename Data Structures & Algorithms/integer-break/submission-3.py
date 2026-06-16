class Solution:
    def integerBreak(self, n: int) -> int:
        memo = {2 : 1}
        def dfs(total) :
            if total in memo :
                return memo[total]

            res = 0
            for num in range(2, total) :
                tmp = dfs(total - num) * num
                res = max(res, tmp,(total - num) * num)

            memo[total] = res
            return res

        return dfs(n)

