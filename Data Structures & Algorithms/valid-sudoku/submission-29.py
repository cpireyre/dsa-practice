class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [0] * 9
        cols = [0] * 9
        squa = [0] * 9
        idx = lambda r,c: 3*(r//3) + c//3
        for r,c in product(range(9),range(9)):
            if board[r][c] == '.': continue
            mask = 1 << (int(board[r][c]) - 1)
            if rows[r] & mask: return False
            if cols[c] & mask: return False
            if squa[idx(r,c)] & mask: return False
            rows[r] |= mask
            cols[c] |= mask
            squa[idx(r,c)] |= mask
        return True