class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = list(range(n))

        def find(x) :
            if parent[x] != x :
                parent[x] = find(parent[x])
            return parent[x]

        for u, v in edges :
            pu, pv = find(u), find(v)
            if pu != pv :
                parent[pv] = pu
                n -= 1
        
        return n
