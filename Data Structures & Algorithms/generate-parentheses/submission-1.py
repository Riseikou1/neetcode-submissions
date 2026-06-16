class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(path, opening, closing) :
            if opening > n or closing > n : return 
            if len(path) == n * 2 :
                res.append("".join(path))
                return

            if opening > closing :
                dfs(path + [")"], opening, closing + 1)
            dfs(path + ["("], opening + 1, closing)

        dfs(["("], 1, 0)
        return res
