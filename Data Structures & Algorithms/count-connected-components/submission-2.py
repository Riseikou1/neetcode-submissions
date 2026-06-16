class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        res = n  # initially every nodes are their own component

        def find(x) :
            if parent[x] != x :
                parent[x] = find(parent[x])
            return parent[x]

        for u, v in edges :
            root_u = find(u)
            root_v = find(v)

            if root_u != root_v :
                parent[root_u] = root_v
                res -= 1  # and reduce the count when union happens.
        
        return res