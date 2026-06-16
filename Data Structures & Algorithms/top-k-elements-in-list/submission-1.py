class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        temuujin = {}
        heap = []
        for num in nums :
            temuujin[num] = temuujin.get(num,0) + 1


        for key, val in temuujin.items():
            heapq.heappush(heap,(-val,key))
        
        res = []
        while(len(res)<k):
            res.append(heapq.heappop(heap)[1])
        return res
