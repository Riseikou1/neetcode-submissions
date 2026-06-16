class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        heap = [(0, 0, 0)]  # diff, r, c
        visited = set()

        while heap :
            diff, r, c = heapq.heappop(heap)    
            if r == rows - 1 and c == cols - 1 :
                return diff
            if (r, c) in visited :
                continue
            visited.add((r, c))
            for dr, dc in directions :
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited :
                    dist = abs(heights[r][c] - heights[nr][nc])
                    heapq.heappush(heap, (max(dist, diff), nr, nc))

        return 0
