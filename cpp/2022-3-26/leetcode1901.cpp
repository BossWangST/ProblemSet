#include <iostream>
#include <utility>
#include <vector>
using namespace std;
int x_dir[4] = {-1, 0, 1, 0};
int y_dir[4] = {0, 1, 0, -1};
/*
 *[[48,36,35,17,48],
   [38,28,38,26,24],
   [15,9,33,32,6],
   [49,4,8,10,41]]
 *
 * [[25,37,23,37,19],
 *  [45,19,2,43,26],
 *  [18,1,37,44,50]]
 *
 * [[1,2,6],
 *  [3,4,5]]
 *
 *
 * */
class Solution {
public:
    int get_max(vector<vector<int>>& mat, int mid) {
        int max_num = -1000000001;
        int max_index = -1;
        for (int i = 0; i < mat.size(); i++)
            if (mat[i][mid] > max_num) {
                max_num = mat[i][mid];
                max_index = i;
            }
        return max_index;
    }
    vector<int> findPeakGrid(vector<vector<int>>& mat) {
        int n = mat.size();
        int m = mat[0].size();
        int left = 0;
        int right = m - 1;
        int mid;
        int mid_col_max_index;
        while (left < right) {
            mid = (left + right) / 2;
            mid_col_max_index = get_max(mat, mid);
            if (mid < m - 1 &&
                mat[mid_col_max_index][mid] < mat[mid_col_max_index][mid + 1]) {
                left = mid + 1;
            } else if (mid > 1 && mat[mid_col_max_index][mid] <
                                      mat[mid_col_max_index][mid - 1]) {
                right = mid - 1;
            } else
                return vector<int>({mid_col_max_index, mid});
        }
        mid_col_max_index = get_max(mat, left);
        return vector<int>({mid_col_max_index, left});
        /*
        int n = mat.size();
        int m = mat[0].size();
        vector<vector<int>> mark(n, vector<int>(m, 0));
        int next_x, next_y;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                for (int k = 0; k < 4; k++) {
                    next_x = i + x_dir[k];
                    next_y = j + y_dir[k];
                    if (next_x < 0 || next_y < 0 || next_x >= n ||
                        next_y >= m) {
                        mark[i][j]++;
                    } else {
                        if (mat[i][j] > mat[next_x][next_y]) mark[i][j]++;
                    }
                }
                if (mark[i][j] == 4) return vector<int>({i, j});
            }
        }
        return vector<int>({-1, -1});
        */
    }
};
int main() {
    vector<vector<int>> mat({{1, 2, 6}, {3, 4, 5}});
    vector<int> res = (new Solution)->findPeakGrid(mat);
    cout << res[0] << " " << res[1] << endl;
    return 0;
}

