class Solution:
    def uniquePathsWithObstacles(self, grid : List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        if grid[0][0] == 1 or grid[rows -1][cols - 1] == 1 : return 0
        grid[rows - 1][cols - 1] = 1

        for r in range(rows - 1, -1, -1) :
            for c in range(cols - 1, -1, -1) :
                if r == rows - 1 and c == cols - 1 : continue

                if grid[r][c] == 1 : grid[r][c] = 0

                else :
                    down = grid[r + 1][c] if r + 1 < rows else 0
                    right = grid[r][c + 1] if c + 1 < cols else 0
                    grid[r][c] = down + right

        return grid[0][0]
