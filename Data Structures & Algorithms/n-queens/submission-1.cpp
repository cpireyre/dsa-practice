class Solution {
    vector<vector<string>> res;
    vector<string> board;
    vector<bool> col, diag1, diag2;

    void dfs(int r, int n) {
        if (r == n) {
            res.push_back(board);
            return;
        }

        for (int c = 0; c < n; c++) {
            if (col[c] || diag1[r + c] || diag2[r - c + n])
                continue;

            col[c] = diag1[r + c] = diag2[r - c + n] = true;
            board[r][c] = 'Q';

            dfs(r + 1, n);

            board[r][c] = '.';
            col[c] = diag1[r + c] = diag2[r - c + n] = false;
        }
    }

public:
    vector<vector<string>> solveNQueens(int n) {
        board.assign(n, string(n, '.'));
        col.assign(n, false);
        diag1.assign(2 * n, false);
        diag2.assign(2 * n, false);

        dfs(0, n);
        return res;
    }
};