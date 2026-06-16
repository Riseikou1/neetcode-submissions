class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = defaultdict(list)
        for idx, (nume, deno) in enumerate(equations) :
            adj[nume].append([deno, values[idx]])
            adj[deno].append([nume, 1/values[idx]])

        def bfs(source, target) :
            if source not in adj or target not in adj : 
                return -1
            q = deque([[source, 1]])
            visited = set([source])

            while q :
                node, weight = q.popleft()
                if node == target : 
                    return weight
                for nei, nei_weight in adj[node] :
                    if nei not in visited :
                        q.append([nei, nei_weight * weight])
                        visited.add(nei)
            return -1

        return [bfs(q[0], q[1]) for q in queries]
