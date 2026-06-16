class Solution:
    def tribonacci(self, n: int) -> int:
        memo = {}
        def dfs(num) :
            if num in memo : return memo[num]
            if num <= 2 :
                return 1 if num != 0 else 0
            
            res = dfs(num - 2) + dfs(num - 1) + dfs(num - 3)

            memo[num] = res
            return res

        return dfs(n)


