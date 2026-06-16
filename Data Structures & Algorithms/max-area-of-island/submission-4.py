class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        max_area = 0

        def helper(row, col) :
            count = 0
            q = deque([(row, col)])
            grid[row][col] = 0

            while q :
                r, c = q.popleft()
                count += 1
                for dr, dc in directions :
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1 :
                        grid[nr][nc] = 0
                        q.append((nr, nc))

            return count

        for r in range(rows) :
            for c in range(cols) :
                if grid[r][c] == 1 :
                    max_area = max(max_area, helper(r, c))

        return max_area
