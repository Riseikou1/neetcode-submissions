class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(r, c, idx) :
            if idx == len(word) - 1:
                return True

            char = board[r][c]
            board[r][c] = "#"

            for dr, dc in directions :
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != "#" and board[nr][nc] == word[idx + 1]:
                    if dfs(nr, nc, idx + 1) :
                        board[r][c] = char
                        return True

            board[r][c] = char
            return False

        for r in range(rows) :
            for c in range(cols) :
                if board[r][c] == word[0] :
                    if dfs(r, c, 0) :
                        return True

        return False
