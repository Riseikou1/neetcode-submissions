class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        q = deque()

        def bfs():
            while q:
                r, c = q.popleft()
                board[r][c] = "T"
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == "O" :
                        q.append((nr, nc))

        for r in range(rows) :
            for c in [0, cols - 1] :
                if board[r][c] == "O" :
                    q.append((r, c))
        
        for c in range(cols) :
            for r in [0, rows - 1] :
                if board[r][c] == "O" :
                    q.append((r, c))

        bfs()
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"
