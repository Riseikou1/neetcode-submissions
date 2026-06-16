class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n, node = len(points) , 0
        visited = [False] * n
        dist = [float('inf')] * n
        edges, res = 0, 0

        while edges < n - 1 :
            visited[node] = True
            nextNode = -1
            for i in range(n) :
                if visited[i] : continue
                curDist = (abs(points[i][0] - points[node][0]) + 
                    abs(points[i][1] - points[node][1])) 

                dist[i] = min(dist[i] ,curDist)
                if nextNode == -1 or dist[i] < dist[nextNode] :
                    nextNode = i

            res += dist[nextNode]
            node = nextNode
            edges += 1

        return res