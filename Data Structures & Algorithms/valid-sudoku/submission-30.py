class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [0] * 9
        squa = [0] * 9
        cols = [0] * 9
        for r,c in product(range(9),range(9)):
            if board[r][c] == '.': continue
            mask = 1 << (int(board[r][c]) - 1)
            if rows[r] & mask: return False
            if cols[c] & mask: return False
            if squa[(r//3)*3 + c//3] & mask: return False
            rows[r] |= mask
            cols[c] |= mask
            squa[(r//3)*3 + c//3] |= mask
        return True