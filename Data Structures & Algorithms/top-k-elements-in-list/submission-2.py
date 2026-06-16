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
                heapq.heappushpop(heap,(val,key))
        
        return [h[1] for h in heap]


