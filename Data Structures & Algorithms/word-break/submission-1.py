class Node :
    def __init__(self) :
        self.children = {}
        self.word = False

    def insert(self, word) :
        cur = self
        for char in word :
            if char not in cur.children :
                cur.children[char] = Node()
            cur = cur.children[char]
        cur.word = True

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        root = Node()
        max_len = 0
        n = len(s)
        dp = [False] * (n + 1)
        dp[-1] = True

        for word in wordDict :
            root.insert(word)
            max_len = max(max_len, len(word))

        for i in range(n - 1, -1, -1) :
            node = root
            for j in range(i, min(n, i + max_len)) :
                if s[j] not in node.children :
                    break
                node = node.children[s[j]]
                if node.word and dp[j + 1] :
                    dp[i] = True
                    break

        return dp[0]