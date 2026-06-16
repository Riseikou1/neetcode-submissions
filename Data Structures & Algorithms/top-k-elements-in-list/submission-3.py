class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        temuujin = {}
        heap = []
        for num in nums :
            temuujin[num] = temuujin.get(num,0) + 1

        
        for key, val in temuujin.items():
            if len(heap) < k :
                heapq.heappush(heap,(val,key))
            else :
                heapq.heappush(heap,(val,key))
                heapq.heappop(heap)
        
        return [h[1] for h in heap]


