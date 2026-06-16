class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash_set = set()
        res = 0
        l = 0

        for char in s :
            while char in hash_set :
                hash_set.remove(s[l])
                l += 1
            hash_set.add(char)
            res = max(res, len(hash_set))

        return res
