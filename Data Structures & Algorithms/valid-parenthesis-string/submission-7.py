class Solution:
    def checkValidString(self, s: str) -> bool:
        memo = {}
        def dfs(idx, left) :
            if idx == len(s) : return left == 0
            if (idx, left) in memo :
                return memo[(idx, left)]

            if left < 0 : return False

            if s[idx] == "(" :
                res = dfs(idx + 1, left + 1)
            elif s[idx] == ")" :
                res = dfs(idx + 1, left - 1)
            else :
                res = dfs(idx + 1, left - 1) or dfs(idx + 1, left + 1) or dfs(idx + 1, left)
            
            memo[(idx, left)] = res
            return res

        return dfs(0, 0)
