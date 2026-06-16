class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def dfs(remaining) :
            if remaining in memo :
                return memo[remaining]
            
            if remaining <= 1 : return 1

            steps = dfs(remaining - 1) + dfs(remaining - 2)

            return steps 

        return dfs(n)
