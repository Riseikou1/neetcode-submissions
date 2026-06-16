class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        resLen = 0

        def helper(l, r) :
            nonlocal resLen, res
            while l >= 0 and r < len(s) and s[l] == s[r] : 
                if r - l + 1 > resLen :
                    resLen = r - l + 1
                    res = s[l : r + 1]
                l -= 1
                r += 1

        for idx in range(len(s)) :
            # for odd length ones
            helper(idx, idx)
            # for even length
            helper(idx, idx + 1)

        return res