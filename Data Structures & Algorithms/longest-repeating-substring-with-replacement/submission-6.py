class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        res = 0
        max_count = 0
        temuujin = {}
        for r in range(len(s)):

            temuujin[s[r]] = temuujin.get(s[r],0) + 1
            max_count = max(max_count,temuujin[s[r]])

            while (r-l+1) - max_count > k :
                temuujin[s[l]] -= 1
                l += 1
                
            res = max(res,(r-l+1))

        return res