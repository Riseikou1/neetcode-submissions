class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        memo = {}

        def dfs(r, c) :
            if (r, c) in memo :
                return memo[(r, c)]
            
            res = 1
            for dr, dc in directions :
                nr, nc = r + dr, c + dc
                if nr in range(rows) and nc in range(cols) and matrix[r][c] < matrix[nr][nc] :
                    res = max(res, 1 + dfs(nr, nc))

            memo[(r, c)] = res
            return res

        res = 0
        for r in range(rows) :
            for c in range(cols) :
                res = max(res, dfs(r, c))

        return res  