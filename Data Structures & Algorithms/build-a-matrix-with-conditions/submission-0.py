class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def topo_sort(edge) :
            indegree = [0] * (k + 1)
            adj = defaultdict(list)
            order = []
            for u, v in edge :
                adj[u].append(v)
                indegree[v] += 1
            
            q = deque([i for i in range(1, k + 1) if indegree[i] == 0])
            while q :
                node = q.popleft()
                order.append(node)
                for nei in adj[node] :
                    indegree[nei] -= 1
                    if indegree[nei] == 0 :
                        q.append(nei)
            return order

        row_order = topo_sort(rowConditions)
        if len(row_order) != k : return []
        col_order = topo_sort(colConditions)
        if len(col_order) != k : return []

        res = [[0] * k for _ in range(k)]
        colIndex = [0] * (k + 1) 
        for i in range(k) :
            colIndex[col_order[i]] = i

        for i in range(k) :
            res[i][colIndex[row_order[i]]] = row_order[i]

        return res

