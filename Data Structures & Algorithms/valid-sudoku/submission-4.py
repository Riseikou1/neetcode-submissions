class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [0] * 9
        cols = [0] * 9
        blck = [0] * 9

        for r in range(9) :
            for c in range(9) :
                if board[r][c] == "." : continue
                num = int(board[r][c]) - 1
                if ((1 << num) & cols[c]) or ((1 << num) & rows[r]) or ((1 << num & blck[(r // 3) * 3 + (c // 3)])) :
                    return False
                
                cols[c] |= 1 << num
                rows[r] |= 1 << num
                blck[(r // 3) * 3 + (c // 3)] |= 1 << num
        
        return True
