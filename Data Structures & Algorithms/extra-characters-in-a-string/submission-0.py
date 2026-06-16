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
        def dfs(idx) :
            if idx in memo : return memo[idx]
            res = 1 + dfs(idx + 1)
            cur = root
            for j in range(idx, len(s)) :
                if s[j] not in cur.children : break
                cur = cur.children[s[j]]
                if cur.word :
                    res = min(res, dfs(j + 1))
            memo[idx] = res
            return res
            
        return dfs(0)

