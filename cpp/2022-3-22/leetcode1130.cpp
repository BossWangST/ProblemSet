#include <iostream>
#include <stack>
#include <vector>
using namespace std;
class Solution {
public:
    int mctFromLeafValues(vector<int>& arr) {
        /*
         * if a<b<c then we have 2 ways: 'ab c' or 'a bc'
         * sum1=ab+bc   sum2=ac+bc
         * so sum1-sum2=a(b-c)<0
         * sum1 is smaller!
         * So we know that we should always combine leaves from small one to big
         * one
         *
         * And if we get a > b < c , there will be 2 cases: a<c or a>c
         * after calculating, we get that we should always combine 2 smaller
         * ones
         *
         * That's all!
         */
        int n = arr.size();
        stack<int> s;
        int sum = 0;
        for (int i = 0; i < n; i++) {
            if (s.empty())
                s.push(arr[i]);
            else {
                if (arr[i] <= s.top()) {
                    // decending sequence
                    s.push(arr[i]);
                } else {
                    // find the smaller pair
                    if (s.size() < 2) {
                        sum += s.top() * arr[i];
                        s.pop();
                        s.push(arr[i]);
                        continue;
                    }
                    int top_one = s.top();
                    s.pop();
                    int next_top = s.top();
                    s.pop();
                    if (arr[i] > next_top) {
                        sum += top_one * next_top;
                        s.push(next_top);
                        i--;
                    } else {
                        sum += top_one * arr[i];
                        s.push(next_top);
                        s.push(arr[i]);
                    }
                }
            }
        }
        while (s.size() != 1) {
            int top_one = s.top();
            s.pop();
            sum += s.top() * top_one;
        }
        return sum;
    }
};
int main() {
    int arr1[] = {4, 11};
    vector<int> arr;
    for (int i = 0; i < 2; i++) arr.push_back(arr1[i]);
    cout << (new Solution())->mctFromLeafValues(arr) << endl;
    return 0;
}

