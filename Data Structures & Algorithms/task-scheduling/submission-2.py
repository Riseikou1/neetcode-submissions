class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = {}
        for char in tasks :
            count[char] = count.get(char, 0) + 1

        heap, q = [], deque()
        for char, num in count.items() :
            heapq.heappush(heap, (-num, char))

        time = 0
        while heap or q :
            if heap :
                count, el = heapq.heappop(heap)
                if -count - 1 > 0 : 
                    q.append((time + n, el, count + 1))
            
            if q and q[0][0] <= time :
                _, el, count = q.popleft()
                heapq.heappush(heap, (count, el))

            time += 1

        return time
