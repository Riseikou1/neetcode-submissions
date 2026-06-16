class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.'] * n for _ in range(n)]
        res = []
        cols, neg_diag, pos_diag = set(), set(), set()

        def dfs(r, board) :
            if r == n :
                cur_path = ["".join(row) for row in board]
                res.append(cur_path)
                return 

            for c in range(n) :
                if (c not in cols and (r-c) not in neg_diag and (r + c) not in pos_diag) :
                    cols.add(c)
                    board[r][c] = 'Q'
                    pos_diag.add((r + c))
                    neg_diag.add((r - c))

                    dfs(r + 1, board)
                    
                    cols.remove(c)
                    board[r][c] = '.'
                    neg_diag.remove((r - c))
                    pos_diag.remove((r + c))

        dfs(0, board)

        return res

