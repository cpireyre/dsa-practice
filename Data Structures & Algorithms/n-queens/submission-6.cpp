class Solution {
public:
    vector<string> board;
    vector<bool> col,posDiag,negDiag;
    vector<vector<string>> res;

    vector<vector<string>> solveNQueens(int n) {
        board.resize(n,string(n,'.'));
        col.resize(n,false);
        posDiag.resize(2*n,false);
        negDiag.resize(2*n,false);
        f(0,n);
        return res;
    }
    void    f(int r, int n) {
        if (r == n) { res.push_back(board); return; }
        for (int c = 0; c < n; c++) {
            if (col[c] || posDiag[r+c] || negDiag[r-c+n]) continue;
            col[c] = posDiag[r+c] = negDiag[r-c+n] = true;
            board[r][c] = 'Q';
            f(r+1,n);
            board[r][c] = '.';
            col[c] = posDiag[r+c] = negDiag[r-c+n] = false;
        }
    }
};