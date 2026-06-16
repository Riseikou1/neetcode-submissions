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
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        root = Trie()
        for word in dictionary :
            root.add(word)
        
        memo = {len(s) : 0}
        def dfs(idx, cur) :
            if idx in memo :
                return memo[idx]

            res = dfs(idx + 1, cur) + 1

            for i in range(idx, len(s)) :
                if s[i] not in cur.children : break
                cur = cur.children[s[i]]
                if cur.word :
                    res = min(res, dfs(i + 1, cur))

            memo[idx] = res
            return res

        return dfs(0, root)
