from collections import defaultdict
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        res = 0
        visited = set()
        graph = defaultdict(list)
        min_heap = [(0, k)]  # (time, node)

        for u, v, time in times:
            graph[u].append((time, v))

        while min_heap:
            time, node = heapq.heappop(min_heap)
            if node in visited:
                continue
            visited.add(node)
            res = max(res, time)

            for nei_time, nei in graph[node]:
                if nei not in visited:
                    heapq.heappush(min_heap, (time + nei_time, nei))

        return res if len(visited) == n else -1
