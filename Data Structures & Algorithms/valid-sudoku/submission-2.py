class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        cols = defaultdict(set)
        rows = defaultdict(set)
        boxes = defaultdict(set)

        for i in range(len(board)):
            for j in range(len(board)):

                val = board[i][j]
                if val == '.' : continue


                if val in rows[i] or val in cols[j] or val in boxes[(i//3)*3 + j//3] :
                    return False

                cols[j].add(val)
                rows[i].add(val)
                boxes[(i//3)*3 + j//3].add(val)

        return True
