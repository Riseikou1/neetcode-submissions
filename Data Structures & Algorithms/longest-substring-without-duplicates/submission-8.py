class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashset = set()
        res, l = 0, 0
        for char in s :
            while char in hashset :
                hashset.remove(s[l])
                l += 1
            hashset.add(char)
            res = max(res, len(hashset))
        
        return res
