class Solution:
    def climbStairs(self, n: int) -> int:
        self.ans = 0 

        def dfs(remaining) :
            if remaining == 0 : 
                self.ans += 1

            if remaining < 0 : return 

            dfs(remaining - 1)
            dfs(remaining - 2)

        dfs(n)
        return self.ans