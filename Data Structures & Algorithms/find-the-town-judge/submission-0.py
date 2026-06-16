class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        indegree = {i : 0 for i in range(1, n + 1)}
        outdegree = {i : 0 for i in range(1, n + 1)}

        for person, judge in trust :
            indegree[judge] += 1
            outdegree[person] += 1

        res = 0
        for key, val in outdegree.items() :
            if val == 0 : 
                res = key

        if not res : return -1

        return res if indegree[res] == n - 1 else -1

