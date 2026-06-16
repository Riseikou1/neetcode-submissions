class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[float('inf')] * (len(word2) + 1) for _ in range(len(word1) + 1)]

        # Case-1 : if word1 is empty, we insert the remaining letters of word2
        for i in range(len(word2) + 1) :
            dp[len(word1)][i] = len(word2) - i

        # Case-2 : if word2 is empty, we delete the remaining letters of word1.
        for i in range(len(word1) + 1) :
            dp[i][len(word2)] = len(word1) - i 

        for i in range(len(word1) - 1, -1, -1) :
            for j in range(len(word2)-1, -1, -1) :
                if word1[i] == word2[j] :
                    dp[i][j] = dp[i + 1][j + 1]
                else :
                    insert = dp[i][j + 1]
                    delete = dp[i + 1][j]
                    replace = dp[i + 1][j + 1]
                    dp[i][j] = 1 + min(insert, delete, replace)

        return dp[0][0]