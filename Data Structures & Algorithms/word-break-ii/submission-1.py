class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        words = set(wordDict) 
        memo = {len(s) : [""]}

        def dfs(idx) :
            if idx in memo : return memo[idx]
            res = []
            
            for j in range(idx, len(s)) :
                w = s[idx : j + 1]
                if w in words :
                    for strr in dfs(j + 1) :
                        res.append(w + (" " + strr if strr else ""))

            memo[idx] = res
            return res

        return dfs(0)
