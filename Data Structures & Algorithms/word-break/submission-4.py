class Trie :
    def __init__(self) :
        self.children = {}
        self.word = False

    def add(self, word) :
        cur = self
        for char in word :
            if char not in cur.children :
                cur.children[char] = Trie()
            cur = cur.children[char]
        cur.word = True

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        root = Trie()
        for word in wordDict :
            root.add(word)
        memo = {}
        def dfs(idx) :
            if idx >= len(s) :
                return True
            if idx in memo :
                return memo[idx]
            cur = root
            for i in range(idx, len(s)) :
                char = s[i]
                if char not in cur.children : break
                cur = cur.children[char]
                if cur.word :
                    if dfs(i + 1) :
                        memo[idx] = True
                        return True

            memo[idx] = False
            return False

        return dfs(0)
