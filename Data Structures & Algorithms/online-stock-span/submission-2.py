class StockSpanner:
    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        self.stack.append(price)
        if not self.stack :
            return None
        
        j = len(self.stack) - 2
        while j >= 0 and self.stack[j] <= price :
            j -= 1

        return len(self.stack) - j - 1

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)