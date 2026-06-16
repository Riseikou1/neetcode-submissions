class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        min_heap = []
        for count, char in [(-a, 'a'), (-b, 'b'), (-c, 'c')]:
            if count != 0:
                heapq.heappush(min_heap, [count, char])

        res = ""
        while min_heap :
            cur = heapq.heappop(min_heap)
            if len(res) >= 2 and res[-1] == res[-2] == cur[1] :
                if not min_heap : break
                real = heapq.heappop(min_heap)  
                res += real[1]
                heapq.heappush(min_heap, cur)
                if real[0] + 1 != 0 :
                    heapq.heappush(min_heap, [real[0] + 1, real[1]])
            else :
                res += cur[1]
                if cur[0] + 1 != 0 :
                    heapq.heappush(min_heap, [cur[0] + 1, cur[1]])

        return res
