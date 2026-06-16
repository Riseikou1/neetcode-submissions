class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def helper(lst) :
            indegree = [0] * (k + 1)
            adj = defaultdict(list)
            for u, v in lst :
                adj[u].append(v)
                indegree[v] += 1
            q = deque([i for i in range(1, k + 1) if indegree[i] == 0])
            order = []
            while q :   
                node = q.popleft()
                order.append(node)
                for nei in adj[node] :
                    indegree[nei] -= 1
                    if indegree[nei] == 0 :
                        q.append(nei)
            return order

        row_order, col_order = helper(rowConditions), helper(colConditions)
        if len(row_order) != k or len(col_order) != k : return []
        board = [[0] * k for _ in range(k)]
        num_to_col = {num : idx for idx, num in enumerate(col_order)}
        
        # fill the board according to row_order & col_order...
        for r in range(k) :
            which_number = row_order[r]
            for c in range(k) :
                which_col = num_to_col[which_number]
                board[r][which_col] = which_number

        return board
