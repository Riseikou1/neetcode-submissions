class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indegree = [0] * numCourses
        visited = set()

        for src, dst in prerequisites :
            indegree[src] += 1
            graph[dst].append(src)
        
        q = deque([i for i in range(numCourses) if indegree[i] == 0])

        cls_taken = 0
        while q :
            cur = q.popleft()
            cls_taken += 1
            for nei in graph[cur] :
                indegree[nei] -= 1
                if indegree[nei] == 0 :
                    q.append(nei)

        return cls_taken == numCourses