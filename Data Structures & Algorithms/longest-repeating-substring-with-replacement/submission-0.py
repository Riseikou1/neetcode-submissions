class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        temuujin = {}
        res = 0
        l = r = 0
        for r in range(len(s)):
            temuujin[s[r]] = temuujin.get(s[r],0) + 1

            max_count = temuujin[max(temuujin,key=temuujin.get)]

            window_size = r - l + 1

            if window_size - max_count <= k:
                res = max(res,window_size)
            else :
                temuujin[s[l]] -= 1
                l += 1
        
        return res
            
        



