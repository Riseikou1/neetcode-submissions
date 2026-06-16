class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rowss = [0]*9
        colss = [0]*9
        boxes = [0]*9

        for rows in range(9):
            for cols in range(9):
                if board[rows][cols] == '.' : continue

                val = int(board[rows][cols]) - 1
                if(1 << val) & rowss[rows] or (1<<val) & colss[cols] or (1<<val) & boxes[(rows//3)*3 + cols//3]:
                   return False

                rowss[rows] |= (1<<val)
                colss[cols] |= (1<<val)
                boxes[(rows//3)*3 + cols//3] |= (1<<val)

        return True