class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def dfs(idx, total, path) :
            if total == target :
                res.append(path)
                return 

            for i in range(idx, len(candidates)) :
                if i > idx and candidates[i] == candidates[i - 1] : continue
                if total + candidates[i] > target : return 
                dfs(i + 1, total + candidates[i], path + [candidates[i]])

        dfs(0, 0, [])
        return res
