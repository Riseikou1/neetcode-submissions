class Solution:
    def reorganizeString(self, s: str) -> str:
        res = []
        count = {}
        for char in s :
            count[char] = count.get(char, 0) + 1
        
        heap = []
        for char, cnt in count.items() :
            heapq.heappush(heap, (-cnt, char))

        prev = None
        while heap or prev :
            if prev and not heap : return ""
            cnt, char = heapq.heappop(heap)
            cnt += 1
            res.append(char)

            if prev :
                heapq.heappush(heap, prev)
                prev = None

            if cnt :
                prev = (cnt, char)

        return "".join(res)
