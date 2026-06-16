class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if not edges : return [0]
        indegree = [0] * n
        adj = defaultdict(list)

        for node1, node2 in edges :
            adj[node1].append(node2)
            adj[node2].append(node1)
            indegree[node1] += 1
            indegree[node2] += 1

        q = deque([i for i in range(n) if indegree[i] == 1])
        while q :
            if n <= 2 : return list(q)
            for _ in range(len(q)) :
                node = q.popleft()
                n -= 1
                for nei in adj[node] :  
                    indegree[nei] -= 1
                    if indegree[nei] == 1 :
                        q.append(nei)

