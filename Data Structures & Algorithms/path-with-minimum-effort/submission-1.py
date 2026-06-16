class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        min_heap = [[0, 0, 0]]
        visited = set()

        while min_heap : 
            diff, r, c = heapq.heappop(min_heap)
            if (r, c) in visited : continue
            visited.add((r, c))
            if (r, c) == (rows - 1, cols - 1) : return diff

            for dr, dc in directions :
                nr, nc = r + dr, c + dc
                if nr not in range(rows) or nc not in range(cols) or (nr,nc) in visited :
                    continue
                new_diff = max(diff, abs(heights[r][c] - heights[nr][nc]))
                heapq.heappush(min_heap, [new_diff, nr, nc])
