class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        l, r = grid[0][0], rows * cols - 1
        visited = set()
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        def isValid(r, c, m, visited) :
            if r == rows - 1 and c == cols - 1 :
                return True

            visited.add((r, c))

            for dr, dc in directions :
                nr, nc = r + dr, c + dc
                if (0<=nr<rows and 0<=nc<cols and grid[nr][nc] <= m
                    and (nr, nc) not in visited) :
                    if isValid(nr, nc, m, visited) :
                        return True

            return False

        while l < r :
            m = (r + l) // 2
            if isValid(0, 0, m, set()) :
                r = m
            else :
                l = m + 1

        return l