class CountSquares:
    def __init__(self):
        self.pointsCount = defaultdict(lambda : defaultdict(int))

    def add(self, point: List[int]) -> None:
        x, y = point
        self.pointsCount[x][y] += 1

    def count(self, point: List[int]) -> int:
        res = 0
        px, py = point

        for y in self.pointsCount[px] :
            length = py - y
            if length == 0 : continue
            x2, x3 = px - length, px + length

            res += (self.pointsCount[x2][py] * self.pointsCount[x2][y] * self.pointsCount[px][y])

            res += (self.pointsCount[x3][py] * self.pointsCount[x3][y] * self.pointsCount[px][y])

        return res
