class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        directions = [(0, 1),(0, -1),(1,0),(-1,0)]
        indegree = [[0] * cols for _ in range(rows)]

        for r in range(rows) :
            for c in range(cols) :
                for dr, dc in directions :
                    nr, nc = r + dr, c + dc
                    if (0<=nr<rows and 0<=nc<cols and matrix[r][c] > matrix[nr][nc]) :
                        indegree[r][c] += 1

        q = deque([[r, c] for r in range(rows) for c in range(cols) if indegree[r][c] == 0])

        res = 0
        while q :
            for _ in range(len(q)) :
                r, c = q.popleft()
                for dr, dc in directions :
                    nr, nc = r + dr, c + dc
                    if (0<=nr<rows and 0<=nc<cols and matrix[r][c] < matrix[nr][nc]) :
                        indegree[nr][nc] -= 1

                        if indegree[nr][nc] == 0 :
                            q.append([nr, nc])
            res += 1

        return res
