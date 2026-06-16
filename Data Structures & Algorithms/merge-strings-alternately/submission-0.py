class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        l, r = 0, 0

        while l < len(word1) and r < len(word2) :
            res += word1[l]
            res += word2[r]
            l += 1
            r += 1

        res += word1[l :] if l < len(word1) else ""
        res += word2[r :] if r < len(word2) else ""

        return res
