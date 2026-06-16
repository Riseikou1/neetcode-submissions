class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1 : return False
        adj = [[] for _ in range(n)]
        visited = set()
        
        for u, v in edges :
            adj[u].append(v)
            adj[v].append(u)

        def dfs(node, prev) :
            if node in visited :
                return False
            visited.add(node)
            for nei in adj[node] :
                if nei == prev : continue
                if not dfs(nei, node) :
                    return False
            return True
        
        return dfs(0, -1) and len(visited) == n
