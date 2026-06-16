class MinStack:
    def __init__(self):
        self.stack = []
        self.mini = float("inf")

    def push(self, val: int) -> None:
        self.stack.append([val, self.mini])
        self.mini = min(self.mini, val)

    def pop(self) -> None:
        tmp, prev_min = self.stack.pop()
        if tmp == self.mini :
            self.mini = prev_min

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.mini
