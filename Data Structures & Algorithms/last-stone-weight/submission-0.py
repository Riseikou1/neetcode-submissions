class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = []

        for num in stones :
            heapq.heappush(max_heap, -num)
        
        while len(max_heap) > 1 :
            stone1 = heapq.heappop(max_heap)
            stone2 = heapq.heappop(max_heap)
        
            if stone2 > stone1 :
                heapq.heappush(max_heap, stone1 - stone2)

        return abs(max_heap[0]) if max_heap else 0