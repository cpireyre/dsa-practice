class Trie:
    def __init__(self):
        self.children = defaultdict(Trie)
        self.word = False
    def slurp(self, words):
        for w in words:
            root = self
            for c in w: root = root.children[c]
            root.word = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        T = Trie(); T.slurp(words)
        R,C = len(board),len(board[0])
        res = set()
        inside    = lambda r,c: 0 <= r < R and 0 <= c < C
        seen      = lambda r,c: board[r][c] == '#'
        neighbors = lambda r,c: [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]
        def f(r,c,acc,root):
            if root.word: res.add(acc)
            if not inside(r,c) or seen(r,c): return
            if board[r][c] not in root.children: return
            char = board[r][c]
            board[r][c] = '#'
            for n in neighbors(r,c): f(*n,acc+char,root.children[char])
            board[r][c] = char
        for n in product(range(R),range(C)): f(*n,"",T)
        return list(res)