class UnionFind :
    def __init__(self, n) :
        self.n = n
        self.rank = [1] * n
        self.parent = [i for i in range(n)]

    def find(self, x) :
        if x != self.parent[x] :
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, u, v) :
        p1, p2 = self.find(u), self.find(v)
        if p1 == p2 : return False
        self.n -= 1
        if self.rank[p1] < self.rank[p2] :
            p1, p2 = p2, p1
        self.parent[p2] = p1
        self.rank[p1] += self.rank[p2]
        return True

    def isConnected(self) :
        return self.n == 1


class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]] :
        for idx, e in enumerate(edges) :
            e.append(idx)   # [v1, v2, weight, idx]
        edges.sort(key = lambda x : x[2])

        def findMST(index, include) :
            weight = 0
            uf = UnionFind(n)
            if include :
                weight += edges[index][2]
                uf.union(edges[index][0], edges[index][1])

            for i, e in enumerate(edges) :
                if i == index : continue
                if uf.union(e[0], e[1]) :
                    weight += e[2]
            return weight if uf.isConnected() else float('inf')

        mst_weight = findMST(-1, False)
        critical, pseudo = [], []

        for i, e in enumerate(edges) :
            # without this edge
            if findMST(i, False) > mst_weight :
                critical.append(e[3])

            # with this edge.
            elif mst_weight == findMST(i, True) :
                pseudo.append(e[3])

        return [critical, pseudo]

        