class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = []
        for char, count in zip(["a", "b", "c"], [a, b, c]) :
            if count :
                heapq.heappush(heap, (-count, char))
        res = []

        while heap :
            cnt, char = heapq.heappop(heap)
            if len(res) >= 2 and res[-2] == res[-1] == char :
                if not heap : break
                second_cnt, second_char = heapq.heappop(heap)
                heapq.heappush(heap, (cnt, char))
                cnt, char = second_cnt, second_char
            
            cnt += 1
            res.append(char)
            if cnt :
                heapq.heappush(heap, (cnt, char))

        return "".join(res)
