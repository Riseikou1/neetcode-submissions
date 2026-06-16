class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [(0, 1), (0 ,-1), (1, 0), (-1, 0)]
        rows, cols = len(grid), len(grid[0])

        def helper(r, c) :
            if not r in range(rows) or not c in range(cols) or grid[r][c] == 0 :
                return 0

            grid[r][c] = 0

            return 1 + helper(r + 1, c) + helper(r - 1, c) + helper(r, c + 1) + helper(r, c - 1)


        res = 0
        for r in range(rows) :
            for c in range(cols) :
                if grid[r][c] == 1 :
                    res = max(res, helper(r, c))
        
        return res
