class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh_orange_count = 0
        directions = [(0,-1),(0,1),(-1,0),(1,0)]
        q = deque()
        rows, cols = len(grid), len(grid[0])

        for r in range(rows) :
            for c in range(cols) :
                if grid[r][c] == 2 :
                    q.append((r, c))
                elif grid[r][c] == 1 :
                    fresh_orange_count += 1

        if fresh_orange_count == 0 :
            return 0

        time = 0
        while fresh_orange_count and q :
            for _ in range(len(q)) :
                r, c = q.popleft()
                for dr, dc in directions :
                    nr, nc = r + dr, c + dc
                    if 0<=nr<rows and 0<=nc<cols and grid[nr][nc] == 1 :
                        grid[nr][nc] = 2
                        fresh_orange_count -= 1
                        q.append((nr, nc))

            time += 1

        return time if not fresh_orange_count else -1