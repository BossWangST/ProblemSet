#include <iostream>
#include <vector>
using namespace std;
int win_state(int res, char win_char) {
    if (res == -1) {
        if (win_char == 'X')
            return 0;
        else
            return 1;
    } else {
        if (res == 0 && win_char == 'X') return 0;
        if (res == 1 && win_char == 'O') return 1;
        return 2;
    }
}
int chess_check(vector<string>& board) {
    // res <=> -1 - no win
    // 0 - X win only
    // 1 - O win only
    // 2 - X O both win
    int res = -1;
    // check row
    if (board[0][0] != ' ' && board[0][0] == board[0][1] &&
        board[0][1] == board[0][2])
        res = win_state(res, board[0][0]);
    if (board[1][0] != ' ' && board[1][0] == board[1][1] &&
        board[1][1] == board[1][2])
        res = win_state(res, board[1][0]);
    if (board[2][0] != ' ' && board[2][0] == board[2][1] &&
        board[2][1] == board[2][2])
        res = win_state(res, board[2][0]);
    // check col
    if (board[0][0] != ' ' && board[0][0] == board[1][0] &&
        board[1][0] == board[2][0])
        res = win_state(res, board[0][0]);
    if (board[0][1] != ' ' && board[0][1] == board[1][1] &&
        board[1][1] == board[2][1])
        res = win_state(res, board[0][1]);
    if (board[0][2] != ' ' && board[0][2] == board[1][2] &&
        board[1][2] == board[2][2])
        res = win_state(res, board[0][2]);
    // check diagonal
    if (board[0][0] != ' ' && board[0][0] == board[1][1] &&
        board[1][1] == board[2][2])
        res = win_state(res, board[0][0]);
    if (board[0][2] != ' ' && board[0][2] == board[1][1] &&
        board[1][1] == board[2][0])
        res = win_state(res, board[0][2]);
    return res;
}
class Solution {
public:
    bool validTicTacToe(vector<string>& board) {
        vector<pair<int, int>> x_position;
        vector<pair<int, int>> o_position;
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                if (board[i][j] == 'X')
                    x_position.push_back(pair<int, int>(i, j));
                else if (board[i][j] == 'O')
                    o_position.push_back(pair<int, int>(i, j));
            }
        }
        // take turns playing
        if (o_position.size() > 0 && x_position.size() == 0) return false;
        if (x_position.size() - o_position.size() > 1 ||
            x_position.size() - o_position.size() < 0)
            return false;
        int win = chess_check(board);
        switch (win) {
            case -1:
                return true;
            case 0:
                if (x_position.size() <= o_position.size())
                    return false;
                else
                    return true;
            case 1:
                if (x_position.size() > o_position.size())
                    return false;
                else
                    return true;
            case 2:
                return false;
        }
        return false;
    }
};
/*
 * xxx
 * xoo
 * oo
 *
 *
 *
 *
 *
 * */
int main() { return 0; }

