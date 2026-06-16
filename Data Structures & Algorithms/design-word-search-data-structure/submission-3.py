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

class WordDictionary:
    def __init__(self):
        self.root = Trie()

    def addWord(self, word: str) -> None:
        self.root.add(word)

    def search(self, word: str) -> bool:
        def dfs(i, j, cur) :
            for k in range(i, j + 1) :
                if word[k] == '.' : # shits happens.
                    for child in cur.children.values() :
                        if dfs(k + 1, j, child) :
                            return True
                    return False

                else :
                    if word[k] not in cur.children :
                        return False
                    cur = cur.children[word[k]]
                
            return cur.word

        return dfs(0, len(word) - 1, self.root)
