class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1 : return False
        adj = [[] for _ in range(n)]
        visited = set([0])

        for u, v in edges :
            adj[u].append(v)
            adj[v].append(u)

        q = deque([(0, -1)])
        while q :
            node, parent = q.popleft()
            for nei in adj[node] :
                if nei == parent : continue
                if nei in visited : return False
                visited.add(nei)
                q.append((nei, node))
        
        return len(visited) == n
