class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        def helper(word1, word2) :
            """ a helper function for detecting the lcp in 2 words """
            i = 0
            while i < min(len(word1), len(word2)) :
                if word1[i] != word2[i] :
                    break
                i += 1

            return word1[:i]

        res = strs[0]
        for word in strs :
            for i in range(1, len(strs)) :
                tmp = helper(strs[i], strs[i - 1])
                if len(tmp) < len(res) :
                    res = tmp
        return res
