class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dist = [float('inf')] * (n + 1)
        dist[k] = 0

        for _ in range(n - 1) :
            for u, v, time in times :
                if dist[u] + time < dist[v] :
                    dist[v] = dist[u] + time

        res = max(dist[1:])
        return res if res != float('inf') else -1