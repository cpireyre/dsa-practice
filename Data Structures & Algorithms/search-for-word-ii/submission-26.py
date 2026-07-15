class Trie:
    def __init__(self):
        self.children = defaultdict(Trie)
        self.word = False
    def slurp(self,words):
        for w in words:
            root = self
            for c in w: root = root.children[c]
            root.word = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        T = Trie(); T.slurp(words)
        R,C = len(board),len(board[0])
        inside = lambda r,c: 0<=r<R and 0<=c<C
        neighbors = lambda r,c: [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]
        res = set()
        def f(r,c,root,acc):
            if not inside(r,c): return
            if board[r][c] == '#': return
            if board[r][c] not in root.children: return
            char = board[r][c]
            acc += char; root = root.children[char]
            if root.word: res.add(acc)
            board[r][c] = '#'
            for u in neighbors(r,c): f(*u,root,acc)
            board[r][c] = char
        for u in product(range(R),range(C)): f(*u,T,"")
        return list(res)