class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        min_heap = [[grid[0][0], 0, 0]]  # max_dist so far, r, c 
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        visited = set()
        visited.add((0, 0))

        while True :
            dst, r, c = heapq.heappop(min_heap)
            if r == rows - 1 and c == cols - 1 :
                return dst
            
            for dr, dc in directions :
                nr, nc = r + dr, c + dc
                if (0<=nr<rows and 0<=nc<cols and (nr, nc) not in visited 
                    ) :
                    heapq.heappush(min_heap, [max(dst, grid[nr][nc]), nr, nc])
                    visited.add((nr, nc))


