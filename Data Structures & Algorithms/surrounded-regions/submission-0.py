class DSU :
    def __init__(self, n) :
        self.parent = list(range(n + 1))
        self.size = [1] * (n + 1)
    
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

    def connected(self, u, v) :
        return self.find(u) == self.find(v)

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        dsu = DSU(rows * cols)

        for r in range(rows) :
            for c in range(cols) :
                if board[r][c] != "O" :
                    continue
                
                if r == 0 or r == rows - 1 or c == 0 or c == cols - 1 :
                    dsu.union(rows * cols, r * cols + c)
                else :
                    for dr, dc in directions :
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == "O" :
                            dsu.union(r * cols + c, nr * cols + nc)


        for r in range(rows) :
            for c in range(cols) :
                if dsu.connected(rows * cols, r * cols + c) :
                    board[r][c] = "O" 
                else :
                    board[r][c] = "X"
