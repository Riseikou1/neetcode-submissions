class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict = set(wordDict)
        n = len(s)
        dp = [[] for _ in range(n + 1)]
        dp[n] = [""]
        
        for i in range(len(s) - 1, -1, -1) :
            for j in range(i, n) :
                word = s[i : j + 1]
                if word in wordDict :
                    for w in dp[j + 1] :
                        dp[i].append((word + " " + w) if w else word)

        return dp[0]
