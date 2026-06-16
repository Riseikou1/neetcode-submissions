class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        min_heap = [[0, 0]]
        n = len(points)
        cache = {0 : 0}
        in_mst = set()
        res = 0

        while len(in_mst) < n :
            cost, u = heapq.heappop(min_heap)
            if u in in_mst : continue
            res += cost
            in_mst.add(u)

            for v in range(n) :
                if not v in in_mst :
                    dist = abs(points[v][0] - points[u][0]) + abs(points[v][1] - points[u][1])
                    if dist < cache.get(v, float('inf')) :
                        cache[v] = dist
                        heapq.heappush(min_heap, [dist, v])

        return res