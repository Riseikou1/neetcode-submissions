class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}
        memo[(m - 1, n - 1)] = 1

        def dfs(r, c) :
            if (r, c) in memo : return memo[(r, c)]

            if r >= m or c >= n : 
                return 0

            memo[(r, c)] = dfs(r + 1, c) + dfs(r, c + 1)
            return memo[(r, c)]

        return dfs(0, 0)
