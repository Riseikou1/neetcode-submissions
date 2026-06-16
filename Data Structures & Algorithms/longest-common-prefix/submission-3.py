class Trie :
    def __init__(self) :
        self.children = {}

    def add(self, word) :
        cur = self
        for char in word :
            if char not in cur.children :
                cur.children[char] = Trie()
            cur = cur.children[char]

    def lcp(self, word, prefixLen) :
        cur = self
        for i in range(min(len(word), prefixLen)) :
            if word[i] not in cur.children :
                return i
            cur = cur.children[word[i]]

        return min(len(word), prefixLen)

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1 : return strs[0]
        mini = 0
        for i in range(1, len(strs)) :
            if len(strs[mini]) > len(strs[i]) :
                mini = i

        prefixLen = len(strs[mini])
        root = Trie()
        root.add(strs[mini])

        for i in range(len(strs)) :
            prefixLen = root.lcp(strs[i], prefixLen)
        return strs[0][:prefixLen]


        