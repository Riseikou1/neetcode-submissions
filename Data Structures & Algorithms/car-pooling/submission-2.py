class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        cur_pas = 0
        pending = []
        to_drop = []
        for num_pas, fromm, to in trips :
            heapq.heappush(pending, (fromm, to, num_pas))

        pos = 0
        while pending or to_drop :
            while pending and pending[0][0] == pos :
                fromm, to, num_pas = heapq.heappop(pending)
                heapq.heappush(to_drop, (to, num_pas))
                cur_pas += num_pas
            
            if to_drop and to_drop[0][0] == pos :
                cur_pas -= heapq.heappop(to_drop)[1]

            if cur_pas > capacity :
                return False
            
            pos += 1

        return True
