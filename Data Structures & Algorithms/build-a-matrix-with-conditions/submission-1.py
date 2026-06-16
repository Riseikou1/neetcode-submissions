class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def topo_sort(edges) :
            indegree = [0] * (k + 1)
            order = []
            adj = defaultdict(list)

            for u, v in edges :
                indegree[v] += 1
                adj[u].append(v)

            q = deque([i for i in range(1, k + 1) if indegree[i] == 0])
            while q :
                node = q.popleft()
                order.append(node)
                for nei in adj[node] :
                    indegree[nei] -= 1
                    if indegree[nei] == 0 :
                        q.append(nei)
            return order

        row_order, col_order = topo_sort(rowConditions), topo_sort(colConditions)
        if len(row_order) != k or len(col_order) != k : return []

        col_idx = {num : idx for idx, num in enumerate(col_order)}
        res = [[0] * k for _ in range(k)]

        for i, num in enumerate(row_order) :
            res[i][col_idx[num]] = num

        return res
