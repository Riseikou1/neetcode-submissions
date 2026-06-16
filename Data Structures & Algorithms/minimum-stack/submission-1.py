class MinStack:
    def __init__(self):
        # store the difference between self.min and cur val.
        self.min = float('inf')
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack :
            self.stack.append(0)
            self.min = val
        else : 
            self.stack.append(val - self.min)
            self.min = min(self.min, val)

    def pop(self) -> None:
        pop = self.stack.pop()
        if pop < 0 :
            self.min = self.min - pop

    def top(self) -> int:
        top = self.stack[-1]
        if top < 0 :
            return self.min
        return top + self.min

    def getMin(self) -> int:
        return self.min


# the number is either positive or negative.
# negative means current number is self.min and prev min was smth bigger.
 # in that case, we also need to update self.min

