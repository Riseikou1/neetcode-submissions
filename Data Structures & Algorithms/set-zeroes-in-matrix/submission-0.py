class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows, cols = len(matrix), len(matrix[0])

        row_set = set()
        col_set = set()

        for r in range(rows) :
            for c in range(cols) :
                if not matrix[r][c] :
                    row_set.add(r)
                    col_set.add(c)
        
        for r in range(rows) :
            for c in range(cols) :
                if r in row_set or c in col_set :
                    matrix[r][c] = 0

