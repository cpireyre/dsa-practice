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
        inside = lambda r,c: 0 <= r < R and 0 <= c < C
        neighbors = lambda r,c: [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]
        res = set()
        def f(root,r,c,acc):
            if not inside(r,c): return
            if board[r][c] == '#': return
            if board[r][c] not in root.children: return
            char = board[r][c]
            board[r][c] = '#'
            root = root.children[char]
            acc += char
            if root.word: res.add(acc)
            for u in neighbors(r,c): f(root,*u,acc)
            board[r][c] = char
        for u in product(range(R),range(C)): f(T,*u,"")
        return list(res)