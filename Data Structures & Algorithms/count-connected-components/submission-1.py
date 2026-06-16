class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        visited = [False] * n
        res = 0

        for u, v in edges :
            adj[u].append(v)
            adj[v].append(u)

        def dfs(node) :
            q = deque([node])
            visited[node] = True
            while q :
                cur = q.popleft()
                for nei in adj[cur] :
                    if not visited[nei] :
                        visited[nei] = True
                        q.append(nei)

        for node in range(n) :
            if not visited[node] : 
                dfs(node)
                res += 1

        return res