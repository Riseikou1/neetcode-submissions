class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        rows, cols = len(matrix), len(matrix[0])
        matrix.reverse()

        for r in range(rows) :
            for c in range(r, cols) :
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
