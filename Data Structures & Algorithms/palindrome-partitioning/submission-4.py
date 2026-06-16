class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        res = []
        dp = [[False] * n for _ in range(n)]

        for l in range(1, n + 1) :
            for i in range(n - l + 1) :
                dp[i][i + l - 1] = (s[i] == s[i + l - 1] and (i + 1 > (i + l - 2) or dp[i + 1][i + l - 2]))

        def dfs(idx, path) :
            if idx >= len(s) :
                res.append(path)
                return 

            for i in range(idx, len(s)) :
                if dp[idx][i] :
                    dfs(i + 1, path + [s[idx : i + 1]])

        dfs(0, [])
        return res
