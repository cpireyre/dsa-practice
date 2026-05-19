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
        R,C = len(board),len(board[0])
        T = Trie(); T.slurp(words)
        S = set()
        inside = lambda r,c: 0<=r<R and 0<=c<C
        neighbors = lambda r,c: [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]
        seen = lambda r,c: board[r][c] == '#'
        def f(r,c,node,acc):
            if node.word: S.add(acc)
            if not inside(r,c) or seen(r,c): return
            if board[r][c] not in node.children: return
            char = board[r][c]; board[r][c] = '#'
            for n in neighbors(r,c): f(*n,node.children[char],acc+char)
            board[r][c] = char
        for p in product(range(R),range(C)): f(*p,T,"")
        return list(S)