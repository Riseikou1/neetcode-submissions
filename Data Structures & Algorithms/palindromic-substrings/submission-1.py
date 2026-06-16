class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0

        def helper(l, r) :
            nonlocal res
            while l >= 0 and r < len(s) and s[l] == s[r] :
                l -= 1
                r += 1
                res += 1

        for i in range(len(s)) :
            helper(i, i)
            helper(i, i + 1)

        return res