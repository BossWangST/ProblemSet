#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;
bool cmp(string& s1, string& s2) { return s1.size() > s2.size(); }
class Solution {
public:
    bool isSub(string& t, string& s) {  // check if s is a sub-sequence of t
        if (s.size() > t.size()) return false;
        int len = t.size();
        int t_index = 0;
        bool current_is = false;
        for (int i = 0; i < s.size(); i++) {
            current_is = false;
            while (t_index < len) {
                if (t[t_index++] == s[i]) {
                    current_is = true;
                    break;
                }
            }
            if (!current_is) return false;
        }
        return true;
    }
    bool check(vector<string>& strs, string& s, int index) {
        for (int i = 0; i < strs.size(); i++) {
            if (i == index) continue;
            if (isSub(strs[i], s)) return false;
        }
        return true;
    }
    int findLUSlength(vector<string>& strs) {
        sort(strs.begin(), strs.end(), cmp);
        int n = strs.size();
        for (int i = 0; i < n; i++) {
            if (check(strs, strs[i], i)) return strs[i].size();
        }
        return -1;
    }
};
int main() {
    vector<string> strs({"abcabc", "abcabc", "abcabc", "abc", "abc", "cca"});
    cout << (new Solution)->findLUSlength(strs) << endl;
    return 0;
}

