class Solution:
    def countSubstrings(self, s: str) -> int:
        
        def helper(l, r) :
            count = 0
            while l >= 0 and r < len(s) and s[l] == s[r] :
                l -= 1
                r += 1
                count += 1
            return count

        res = 0
        for i in range(len(s)) :
            res += helper(i, i)
            res += helper(i, i + 1)
        return res