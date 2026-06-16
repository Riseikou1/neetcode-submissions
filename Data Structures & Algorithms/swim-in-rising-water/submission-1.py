class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        self.res = float('inf')

        def dfs(r, c, cur_max, visited):
            if cur_max >= self.res:
                return  # prune worse paths
            
            if r == rows - 1 and c == cols - 1:
                self.res = min(self.res, max(cur_max, grid[r][c]))
                return

            visited.add((r, c))
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                    dfs(nr, nc, max(cur_max, grid[nr][nc]), visited)
            visited.remove((r, c))

        dfs(0, 0, grid[0][0], set())
        return self.res
