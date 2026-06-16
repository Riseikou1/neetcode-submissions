class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}
        def dfs(i) :
            if i == len(s) : return 1
            if s[i] == "0" : return 0
            if i in memo : return memo[i]

            res = dfs(i + 1)  # take single digit.

            if i + 1 < len(s) and int(s[i : i + 2]) <= 26 :
                res += dfs(i + 2)  # take 2 digits.

            memo[i] = res
            return res

        return dfs(0)

                