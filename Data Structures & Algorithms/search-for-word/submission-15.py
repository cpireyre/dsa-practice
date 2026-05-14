class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        R,C = len(board),len(board[0])
        inside = lambda r,c: 0<=r<R and 0<=c<C
        neighbors = lambda r,c: [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]
        def f(r,c,acc):
            if acc == word: return True
            if len(acc) > len(word): return False
            if not inside(r,c): return False
            if board[r][c] == "#": return False
            char = board[r][c]
            acc += char
            board[r][c] = "#"
            if any(f(*n,acc) for n in neighbors(r,c)): return True
            board[r][c] = char
        return any(f(*S,"") for S in product(range(R),range(C)))