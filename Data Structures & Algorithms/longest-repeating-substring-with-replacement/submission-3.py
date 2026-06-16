class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        temuujin = {}
        res = 0
        l = max_count = 0
        for r in range(len(s)):
            temuujin[s[r]] = temuujin.get(s[r],0) + 1

            max_count = max(max_count,temuujin[s[r]])

            while (r-l+1) - max_count > k :
                temuujin[s[l]] -= 1
                l += 1

            res = max(res,r-l+1)

        return res
            
        



