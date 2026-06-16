class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        res = 0
        temuujin = {}
        for r in range(len(s)):

            temuujin[s[r]] = temuujin.get(s[r],0) + 1

            max_count = max(v for _,v in temuujin.items())

            if (r-l+1) - max_count > k :
                temuujin[s[l]] -= 1
                l += 1
                
            res = max(res,(r-l+1))

        return res