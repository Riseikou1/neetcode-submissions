class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        res = []
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        pac_set, atl_set = set(), set()

        def dfs(r, c, path_set) :
            if r < 0 or r >= rows or c < 0 or c >= cols or (r, c) in path_set :
                return 

            path_set.add((r, c))

            for dr, dc in directions :
                nr, nc = r + dr, c + dc
                if (nr in range(rows) and nc in range(cols) and
                    heights[r][c] <= heights[nr][nc]):
                    dfs(nr, nc, path_set)

        for r in range(rows) :
            dfs(r, 0, pac_set)
            dfs(r, cols - 1, atl_set)

        for c in range(cols) :
            dfs(rows - 1, c, atl_set)
            dfs(0, c, pac_set)

        for r in range(rows) :
            for c in range(cols) :
                if (r, c) in pac_set and (r, c) in atl_set :
                    res.append([r, c])

        return res