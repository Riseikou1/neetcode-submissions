class Solution:
    def totalNQueens(self, n: int) -> List[List[str]]:
        self.res = 0
        neg_diag, pos_diag, col = set(), set(), set()

        def dfs(r) :
            if r == n :
                self.res += 1
                return 

            for c in range(n) :
                if (c not in col and(r + c) not in pos_diag and (r - c) not in neg_diag) :

                    neg_diag.add((r - c))
                    pos_diag.add((r + c))
                    col.add(c)
                    dfs(r + 1)
                    neg_diag.remove((r - c))
                    pos_diag.remove((r + c))
                    col.remove(c)

        dfs(0)
        return self.res
