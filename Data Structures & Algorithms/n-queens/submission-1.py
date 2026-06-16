class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        pos_diag, neg_diag, cols = set(), set(), set()
        board = [["."] * n for _ in range(n)]
        res = []

        def dfs(r) :
            if r >= n :
                res.append(["".join(row) for row in board])
                return 
            
            for c in range(n) :
                if c not in cols and (r - c) not in neg_diag and (r + c) not in pos_diag :
                    board[r][c] = "Q"
                    cols.add(c)
                    neg_diag.add(r - c)
                    pos_diag.add(r + c)

                    dfs(r + 1)

                    cols.remove(c)
                    neg_diag.remove(r - c)
                    pos_diag.remove(r + c)
                    board[r][c] = "."

        dfs(0)
        return res

# in each row, there should be a single queen.
# so after placing a queen at some col_idx, 
# recurse to next row..
