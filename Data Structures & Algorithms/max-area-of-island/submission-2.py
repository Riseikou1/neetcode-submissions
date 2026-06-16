class DSU :
    def __init__(self, n) :
        self.size = [1] * (n + 1)
        self.parent = list(range(n + 1))

    def find(self, node) :
        if self.parent[node] != node :
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, u, v) :
        pu, pv = self.find(u), self.find(v)
        if pu == pv : return False
        if self.size[pu] < self.size[pv] :
            pu, pv = pv, pu
        self.size[pu] += self.size[pv]
        self.parent[pv] = pu
        return True

    def getSize(self, node) :
        return self.size[self.find(node)]

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        dsu = DSU(rows * cols)

        def get_index(r, c) :
            return r * cols + c

        max_area = 0
        for r in range(rows) :
            for c in range(cols) :
                if grid[r][c] == 1 :
                    for dr, dc in directions :
                        nr, nc = r + dr, c + dc
                        if (0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1) :
                            dsu.union(get_index(r, c), get_index(nr, nc))

                    max_area = max(max_area, dsu.getSize(get_index(r, c)))

        return max_area
