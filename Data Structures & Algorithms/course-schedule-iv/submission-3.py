class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        res, memo = [], {}
        adj = [[] for _ in range(numCourses)]
        
        for pre, course in prerequisites :
            adj[pre].append(course)
            memo[(pre, course)] = True

        def dfs(course, target) :
            if (course, target) in memo :
                return memo[(course, target)]

            for pre in adj[course] :
                if pre == target or dfs(pre, target) :
                    memo[(course, target)] = True
                    return True

            memo[(course, target)] = False
            return False

        return [dfs(u, v) for u, v in queries]
