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
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        root = Trie()
        for word in wordDict :
            root.add(word)
            
        memo = {len(s) : [""]}
        def dfs(idx) :
            if idx in memo :
                return memo[idx]
            res = []
            cur = root
            for i in range(idx, len(s)) :
                if s[i] not in cur.children : break
                cur = cur.children[s[i]]
                if cur.word :
                    for suffix in dfs(i + 1) :
                        res.append(s[idx : i+1] + (" " + suffix if suffix else ""))

            memo[idx] = res
            return res

        return dfs(0)