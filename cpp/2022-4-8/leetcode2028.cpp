#include <iostream>
#include <vector>
using namespace std;
class Solution {
public:
    vector<int> missingRolls(vector<int>& rolls, int mean, int n) {
        int m_sum = 0;
        int m = rolls.size();
        for (int i = 0; i < m; i++) m_sum += rolls[i];
        int n_sum = mean * (m + n) - m_sum;
        if (n_sum < n || n_sum > 6 * n) return vector<int>();
        int avg = n_sum / n;
        int left = n_sum % n;
        vector<int> res(n, avg);
        int i = 0;
        while (left > 0) {
            res[i++]++;
            left--;
        }
        return res;
    }
};

int main() {
    vector<int> rolls({4, 5, 6, 2, 3, 6, 5, 4, 6, 4, 5, 1, 6, 3, 1, 4,
                       5, 5, 3, 2, 3, 5, 3, 2, 1, 5, 4, 3, 5, 1, 5});
    vector<int> res = (new Solution)->missingRolls(rolls, 4, 40);
    for (int i = 0; i < res.size(); i++) cout << res[i] << endl;
    return 0;
}

