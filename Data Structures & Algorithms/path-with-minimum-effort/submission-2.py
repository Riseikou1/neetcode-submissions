class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        directions = [(0,1), (0, -1), (1, 0), (-1,0)]
        dist = [float('inf')] * (rows * cols)
        dist[0] = 0
        q = deque([0])
        in_queue = [False] * (rows * cols)
        in_queue[0] = True

        def conv(r, c) :
            return r * cols + c

        while q :
            u = q.popleft()
            in_queue[u] = False
            r, c = divmod(u, cols)
            for dr, dc in directions :
                nr, nc = r + dr, c + dc
                if nr in range(rows) and nc in range(cols) :
                    v = conv(nr, nc)
                    weight = abs(heights[nr][nc] - heights[r][c])
                    new_dist = max(dist[u], weight)
                    if new_dist < dist[v] :
                        dist[v] = new_dist
                        if not in_queue[v] :
                            q.append(v)
                            in_queue[v] = True

        return dist[rows * cols - 1]
