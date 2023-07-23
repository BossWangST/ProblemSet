#include <iostream>
#include <vector>
using namespace std;
int x_dir[4] = {-1, 0, 1, 0};
int y_dir[4] = {0, 1, 0, -1};
class Solution {
public:
    void check(int i, int j, vector<vector<bool>>& visited,
               vector<vector<char>>& board) {
        int next_x, next_y;
        int n = board.size();
        int m = board[0].size();
        for (int k = 0; k < 4; k++) {
            next_x = i + x_dir[k];
            next_y = j + y_dir[k];
            if (next_x < 0 || next_y < 0 || next_x >= n || next_y >= m ||
                board[next_x][next_y] != 'X' || visited[next_x][next_y])
                continue;
            visited[next_x][next_y] = true;
            check(next_x,next_y,visited,board);
        }
    }
    int countBattleships(vector<vector<char>>& board) {
        int res = 0;
        int n = board.size();
        int m = board[0].size();
        vector<vector<bool>> visited(n, vector<bool>(m, false));
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (!visited[i][j] && board[i][j] == 'X') {
                    res++;
                    visited[i][j] = true;
                    check(i, j, visited, board);
                }
            }
        }
        return res;
    }
};
int main() {
    vector<vector<char>> board(
        {{'X', '.', '.', 'X'}, {'.', '.', '.', 'X'}, {'.', '.', '.', 'X'}});
    cout << (new Solution)->countBattleships(board) << endl;
    return 0;
}

