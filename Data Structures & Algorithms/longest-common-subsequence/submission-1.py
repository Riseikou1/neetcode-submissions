class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) < len(text2) :
            text1, text2 = text1, text2

        dp = [0] * (len(text2) + 1)    
        
        for i in range(len(text1) -1, -1, -1) :
            prev = 0
            for j in range(len(text2)- 1, -1, -1) :
                temp = dp[j]

                if text1[i] == text2[j] :
                    dp[j] = 1 + prev   # ==> prev == [i + 1][j + 1]

                else :
                    # in here dp[j] is casually being equal to [i+1][j]
                    # cause we have a single 1d list, so before updating, it means it is a prev state.
                    dp[j] = max(dp[j], dp[j + 1])

                prev = temp

        return dp[0]