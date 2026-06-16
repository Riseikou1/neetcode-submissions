class Trie :
    def __init__(self) :
        self.children = {}
        self.word = None

    def add(self, word) :
        cur = self
        for char in word :
            if char not in cur.children :
                cur.children[char] = Trie()
            cur = cur.children[char]
        cur.word = word

    def search(self, word) :
        cur = self
        for char in word :
            if char not in cur.children :
                return False
            cur = cur.children[char]
        return cur.word == word

    def start(self, word) :
        cur = self
        for char in word :
            if char not in cur.children :
                return False
            cur = cur.children[char]
        return True

class PrefixTree:
    def __init__(self):
        self.root = Trie()

    def insert(self, word: str) -> None:
        self.root.add(word)

    def search(self, word: str) -> bool:
        return self.root.search(word)

    def startsWith(self, prefix: str) -> bool:
        return self.root.start(prefix)
