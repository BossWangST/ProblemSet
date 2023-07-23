//
// Created by bossw on 2022/10/19.
//

#include<iostream>
#include<vector>

using namespace std;

class Solution {
public:
    int longestCommonSubsequence(string text1, string text2) {
        int m = text1.length();
        int n = text2.length();
        vector<vector<int>> table(m + 1, vector<int>(n + 1, 0));
        for (int i = 1; i < m + 1; i++) {
            for (int j = 1; j < n + 1; j++) {
                if (text1[i - 1] == text2[j - 1]) {
                    table[i][j] += table[i - 1][j - 1] + 1;
                } else {
                    table[i][j] = max(table[i - 1][j], table[i][j - 1]);
                }
            }
        }
        return table[m][n];
    }
};

int main(void) {
    string text1 = "abcde";
    string text2 = "ace";
    cout << (new Solution)->longestCommonSubsequence(text1, text2) << endl;
    return 0;
}