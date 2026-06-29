class Trie:
    def __init__(self):
        self.children = defaultdict(Trie)
        self.word = False
    def slurp(self,ws):
        for w in ws:
            root = self
            for c in w: root = root.children[c]
            root.word = True
            
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        R,C = len(board),len(board[0])
        G = Trie(); G.slurp(words)
        res = set()
        inside = lambda r,c: 0 <= r < R and 0 <= c < C
        neighbors = lambda r,c: [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]
        def f(r,c,root,acc):
            if root.word: res.add(acc)
            if not inside(r,c): return
            char = board[r][c]
            if char not in root.children: return
            if board[r][c] == '#': return
            board[r][c] = '#'
            root = root.children[char]; acc += char
            for u in neighbors(r,c): f(*u,root,acc)
            board[r][c]  = char
        for u in product(range(R),range(C)): f(*u,G,"")
        return list(res)