class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        min_heap = [-num for num in count.values()]
        heapq.heapify(min_heap)
        q = deque()
        time = 0

        while min_heap or q :
            time += 1
            
            if min_heap :
                cur = 1 + heapq.heappop(min_heap)
                if cur :
                    q.append((cur, time + n))

            if q and q[0][1] == time :
                heapq.heappush(min_heap, q.popleft()[0])

        return time
