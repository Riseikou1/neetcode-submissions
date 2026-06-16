class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        min_heap = [[-cnt, char] for char, cnt in count.items()]
        heapq.heapify(min_heap)
        res = ""
        prev = None
        while min_heap or prev :
            if not min_heap and prev : return ""
            cnt, char = heapq.heappop(min_heap)
            res += char
            cnt += 1
            if prev :
                heapq.heappush(min_heap, prev)
                prev = None
            if cnt :
                prev = [cnt, char]
        
        return res
