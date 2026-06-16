class StockSpanner:
    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        days = 0
        while self.stack and self.stack[-1][0] <= price :
            days += self.stack.pop()[1]

        self.stack.append([price, days + 1])
        return days + 1

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)