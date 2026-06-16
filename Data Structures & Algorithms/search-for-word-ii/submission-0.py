class Node :
    def __init__(self) :
        self.children = {}
        self.word = None

    def add(self,word) :
        cur = self
        for char in word :
            if not char in cur.children :
                cur.children[char] = Node()
            cur = cur.children[char]
        cur.word = word

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.root = Node()
        res = []
        rows, cols = len(board) , len(board[0])
        for word in words :
            self.root.add(word)

        def dfs(r,c,cur) :
            char = board[r][c]
            if char not in cur.children :
                return
            
            next_word = cur.children[char]
            if next_word.word :
                res.append(next_word.word)
                next_word.word = None


            board[r][c] = '#'
            for dr, dc in zip([0,0,-1,1],[1,-1,0,0]) :
                nr, nc = r + dr , c + dc
                if 0<=nr<rows and 0<=nc<cols and board[nr][nc] != '#' :
                    dfs(nr, nc ,next_word)

            board[r][c] = char

            if not next_word.children :
                del cur.children[char]
        
        for r in range(rows) :
            for c in range(cols) :
                dfs(r, c, self.root)
        return res
