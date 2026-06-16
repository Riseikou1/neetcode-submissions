class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = Counter(s)
        min_heap = []
        for key, val in counter.items() :
            heapq.heappush(min_heap, [-val, key])
        q = deque()
        res = ""
        cd = 0

        while min_heap or q :
            if min_heap :
                val, key = heapq.heappop(min_heap)
                res += key
                if val + 1 :
                    q.append([val + 1, key, cd + 2])

            cd += 1
            if q and q[0][-1] == cd :
                val, key, _ = q.popleft()
                heapq.heappush(min_heap, [val, key])

        return "" if res[-1] == res[-2] else res
