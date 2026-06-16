class CountSquares:
    def __init__(self):
        self.points = []
        self.pointsCount = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.points.append(point)
        self.pointsCount[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        res = 0
        px, py = point

        for x, y in self.points :
            if abs(px - x) != abs(py - y) or (x == px) or (y == py) :
                continue

            res += self.pointsCount[(px, y)] * self.pointsCount[(x, py)]

        return res
