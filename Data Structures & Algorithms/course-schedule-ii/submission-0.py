class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        graph = defaultdict(list)
        indegree = [0] * numCourses
        visited = set()
        res = []

        for src, dst in prerequisites :
            indegree[src] += 1
            graph[dst].append(src)
        
        q = deque([i for i in range(numCourses) if indegree[i] == 0])

        while q :
            cur = q.popleft()
            res.append(cur)
            for nei in graph[cur] :
                indegree[nei] -= 1
                if indegree[nei] == 0 :
                    q.append(nei)

        return res if len(res) == numCourses else []