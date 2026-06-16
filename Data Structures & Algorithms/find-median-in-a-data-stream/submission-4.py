class MedianFinder:
    def __init__(self):
        self.bigger = []
        self.smaller = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.smaller, -num)
        heapq.heappush(self.bigger, -heapq.heappop(self.smaller))

        if len(self.bigger) > len(self.smaller) + 1 :
            heapq.heappush(self.smaller, -heapq.heappop(self.bigger))

    def findMedian(self) -> float:
        if len(self.bigger) > len(self.smaller) :
            return self.bigger[0]
        return (self.bigger[0] - self.smaller[0]) / 2
