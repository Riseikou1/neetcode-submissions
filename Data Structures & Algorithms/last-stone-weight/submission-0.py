class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for stone in stones :
            heapq.heappush(heap, -stone)

        while len(heap) >= 2 :
            big1, big2 = heapq.heappop(heap), heapq.heappop(heap)
            if big1 != big2 :
                heapq.heappush(heap, big1 - big2)

        return -heap[0] if heap else 0
