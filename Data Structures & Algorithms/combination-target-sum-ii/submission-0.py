class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(cur_sum, idx, cur_path) :
            if cur_sum == target :
                res.append(list(cur_path))
                return 

            if cur_sum > target or idx >= len(candidates) :
                return 

            for i in range(idx, len(candidates)) :
                if (candidates[i] > target) or candidates[i] + cur_sum > target :
                    break 
                if i > idx and candidates[i] == candidates[i - 1] :
                    continue
                dfs(cur_sum + candidates[i], i + 1, cur_path + [candidates[i]])

        dfs(0, 0, [])
        return res
            