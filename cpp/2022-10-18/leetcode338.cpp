#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    vector<int> countBits(int n) {
        vector<int> res(n + 1);
        res[0] = 0;
        if (n == 0) {
            return res;
        }
        res[1] = 1;
        int flag = 2;// from 2 bits to count
        int counter = 0;
        for (int i = 2; i <= n; i++) {
            res[i] = 1 + res[i - flag];
            // every new num is just adding "1" in the head of the 2's complement
            counter++;
            if (counter == flag) {
                flag *= 2;
                counter = 0;
            }
        }
        return res;
    }
};

int main() {
    int n = 5;
    vector<int> res = (new Solution)->countBits(n);
    for (int i = 0; i < n + 1; i++) {
        cout << res[i] << endl;
    }
    return 0;
}
