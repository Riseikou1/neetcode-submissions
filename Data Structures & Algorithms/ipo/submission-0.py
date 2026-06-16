class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        res = w
        min_heap = []  # capittal, profit.
        for p, c in zip(profits, capital) :
            heapq.heappush(min_heap, [c, p])
        cur = []

        for _ in range(k) :
            while min_heap and min_heap[0][0] <= res :
                cap, pro = heapq.heappop(min_heap)
                heapq.heappush(cur, -pro)

            if cur :
                res += -heapq.heappop(cur)

        return res
