
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for i in board :
            rows = {}
            for num in i :
                if not num == '.':
                    rows[num] = rows.get(num,0) + 1

            for _, val in rows.items():
                if val != 1 :
                    return False
                
        for i in range(len(board)):
            cols = {}
            for sub in board :
                if not sub[i] == '.':
                    cols[sub[i]] = cols.get(sub[i], 0) + 1
            
            for val in cols.values():
                if val != 1 :
                    return False
                

        temuujin = defaultdict(list)
        for row in range(len(board)):
            for col in range(len(board)):
                if board[row][col] != '.':
                    temuujin[(row // 3) * 3 + (col // 3)].append(board[row][col])

        for lst in temuujin.values():
            square = {}
            for num in lst:
                if num in square:
                    return False
                square[num] = 1

        return True