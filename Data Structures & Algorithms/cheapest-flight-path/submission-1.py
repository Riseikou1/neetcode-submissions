class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        heap = [(0, src, 0)]  # cost, node, stops
        adj = defaultdict(list)
        for u, v, w in flights :
            adj[u].append((v, w))
        dist = [[float("inf")] * (k + 2) for _ in range(n)]

        while heap :
            cost, node, stops = heapq.heappop(heap)
            if stops > k + 1 or dist[node][stops] < cost :
                continue
            if node == dst :
                return cost
            if stops == k + 1 : continue

            for nei, nei_weight in adj[node] :
                new_weight = nei_weight + cost
                if new_weight < dist[nei][stops + 1] :
                    dist[nei][stops + 1] = new_weight
                    heapq.heappush(heap, (new_weight, nei, stops + 1))

        return -1
