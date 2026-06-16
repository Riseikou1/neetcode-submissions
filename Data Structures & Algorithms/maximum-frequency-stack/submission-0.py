class FreqStack:
    def __init__(self):
        self.countMap = {}
        self.stacks = {}
        self.max_freq = 0

    def push(self, val: int) -> None:
        valCnt = self.countMap.get(val, 0) + 1
        self.countMap[val] = valCnt
        if valCnt > self.max_freq :
            self.max_freq = valCnt
            self.stacks[self.max_freq] = []
        self.stacks[valCnt].append(val)

    def pop(self) -> int:
        res = self.stacks[self.max_freq].pop()
        if not self.stacks[self.max_freq] :
            self.max_freq -= 1
        self.countMap[res] -= 1
        return res

