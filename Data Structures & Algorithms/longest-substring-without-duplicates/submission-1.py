class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        temuujin = dict()
        l = 0 
        res = 0
        
        for r in range(len(s)):
            if s[r] in temuujin :
                l = max(l,temuujin[s[r]]+1)
            temuujin[s[r]] = r
            res = max(res,r-l+1)

        return res
    