class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        rows, cols = len(matrix), len(matrix[0])
        self.board = [[0] * (cols + 1) for _ in range(rows + 1)]

        for r in range(1, rows + 1) :
            prefix_sum = 0
            for c in range(1, cols + 1) :
                prefix_sum += matrix[r - 1][c - 1]
                self.board[r][c] = prefix_sum + self.board[r - 1][c]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        r1, r2, c1, c2 = row1 + 1, row2 + 1, col1 + 1, col2 + 1

        bottomleft = self.board[r2][c2]
        Left = self.board[r2][c1 - 1]
        Top = self.board[r1 - 1][c2]
        topLeft = self.board[r1 - 1][c1 - 1]

        return bottomleft - Left - Top + topLeft


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)