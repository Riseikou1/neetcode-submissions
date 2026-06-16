class Solution:
    def tribonacci(self, n: int) -> int:
        memo = {0 : 0, 1 : 1, 2 : 1}

        def dfs(num) :
            if num in memo :
                return memo[num]

            memo[num] = dfs(num - 1) + dfs(num - 2) + dfs(num - 3)
            return memo[num]

        return dfs(n)
