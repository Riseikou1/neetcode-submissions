class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = defaultdict(list)
        for pre, crs in prerequisites :
            adj[crs].append(pre)

        def dfs(crs) :
            if not crs in preMap :
                preMap[crs] = set()
                for prereq in adj[crs] :
                    preMap[crs] |= dfs(prereq)
                preMap[crs].add(crs)
            return preMap[crs]

        preMap = defaultdict(set)
        for crs in range(numCourses) :
            dfs(crs)

        res = []
        for u, v in queries :
            res.append(u in preMap[v])
        return res      