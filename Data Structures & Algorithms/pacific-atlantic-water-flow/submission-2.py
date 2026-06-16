class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        rows, cols = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(r, c, seen) :
            if r < 0 or r >= rows or c < 0 or c >= cols or (r, c) in seen : 
                return

            seen.add((r, c))
            for dr, dc in directions :
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and heights[nr][nc] >= heights[r][c] :
                    dfs(nr, nc, seen)

        # for pac
        for r in range(rows) :
            dfs(r, 0, pac)
            dfs(r, cols - 1, atl)
        for c in range(cols) :
            dfs(0, c, pac)
            dfs(rows - 1, c, atl)

        return list(pac & atl)
