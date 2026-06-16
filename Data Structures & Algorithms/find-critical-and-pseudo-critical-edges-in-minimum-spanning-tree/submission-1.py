class UnionFind :
    def __init__(self, n) :
        self.parent = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, x) :
        if x != self.parent[x] :
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, u, v) :
        p1, p2 = self.find(u), self.find(v)
        if p1 == p2 : return False

        if self.rank[p1] < self.rank[p2] :
            p1, p2 = p2, p1
        self.parent[p2] = p1
        self.rank[p1] += self.rank[p2]

        return True

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        edges = [(u,v,w,idx) for idx,(u, v, w) in enumerate(edges)]
        adj = defaultdict(list)
        for u, v, w, idx in edges :
            adj[u].append((v, w, idx))
            adj[v].append((u, w, idx))
        critical, pseudo = [], []

        def minimax(src, dst, exclude_idx) : 
            dist = [float('inf')] * n
            dist[src] = 0
            q = [(0, src)]
            while q :
                max_weight, u = heapq.heappop(q)
                if u == dst : return max_weight
                for v, weight, edge_idx in adj[u] :
                    if edge_idx == exclude_idx: continue
                    new_weight = max(weight, max_weight)
                    if new_weight < dist[v] :
                        dist[v] = new_weight
                        heapq.heappush(q, (new_weight, v))

            return float('inf')
        
        for u, v, w, idx in edges :
            if w < minimax(u,v, idx) :
                critical.append(idx)
            elif w == minimax(u, v, -1) :
                pseudo.append(idx)
        return [critical, pseudo]

