class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0

        def helper(l, r) :
            while l < r and s[l] == s[r] :
                l += 1
                r -= 1
            return l >= r

        for i in range(len(s)) :
            for j in range(i, len(s)) :
                if helper(i, j) :
                    res += 1

        return res