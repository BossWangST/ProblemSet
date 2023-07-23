#include <algorithm>
#include <iostream>
#include <queue>
#include <vector>
using namespace std;
class Solution {
public:
    int minStoneSum(vector<int>& piles, int k) {
        priority_queue<int> q;
        int n = piles.size();
        for (int i = 0; i < n; i++) q.push(piles[i]);
        int sum = 0;
        int top_num;
        for (int i = 0; i < k; i++) {
            top_num = q.top();
            q.pop();
            top_num -= top_num / 2;
            q.push(top_num);
        }
        for (int i = 0; i < n; i++) {
            sum += q.top();
            q.pop();
        }
        return sum;
    }
};
int main() {
    std::cout << "Hello world" << std::endl;
    return 0;
}

