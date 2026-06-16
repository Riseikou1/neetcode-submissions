class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        res = []
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        pac_set, atl_set = set(), set()

        def bfs(starts, visited) :
            q = deque(starts)
            while q :
                r, c = q.popleft()
                visited.add((r, c))    
                for dr, dc in directions :
                    nr, nc = r + dr, c + dc
                    if (nr in range(rows) and nc in range(cols) and (nr, nc) not in visited and
                        heights[r][c] <= heights[nr][nc]):
                        q.append((nr, nc))


        pac_starts = [(r, 0) for r in range(rows)] + [(0, c) for c in range(cols)]
        atl_starts = [(r, cols - 1) for r in range(rows)] + [(rows - 1, c) for c in range(cols)]

        bfs(atl_starts, atl_set)
        bfs(pac_starts, pac_set)

        return list(pac_set & atl_set)

