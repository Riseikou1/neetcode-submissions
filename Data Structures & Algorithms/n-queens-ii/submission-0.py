class Solution:
    def totalNQueens(self, n: int) -> List[List[str]]:
        board = [['.'] * n for _ in range(n)]
        self.res = 0
        neg_diag, pos_diag, col = set(), set(), set()

        def dfs(r, board) :
            if r == n :
                self.res += 1
                return 

            for c in range(n) :
                if (c not in col and board[r][c] != '#' and
                   (r + c) not in pos_diag and (r - c) not in neg_diag) :

                    board[r][c] = '#'
                    neg_diag.add((r - c))
                    pos_diag.add((r + c))
                    col.add(c)
                    dfs(r + 1, board)
                    neg_diag.remove((r - c))
                    pos_diag.remove((r + c))
                    col.remove(c)
                    board[r][c] = '.'

        dfs(0, board)
        return self.res
