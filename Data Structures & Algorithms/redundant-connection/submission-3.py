class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = list(range(len(edges) + 1))

        def find(node) :
            if node != parent[node] :
                parent[node] = find(parent[node])
            return parent[node]
        
        for u, v in edges :
            pu, pv = find(u), find(v)
            if pu != pv :
                parent[pv] = pu
            else :
                return [u, v]
        
        return []
