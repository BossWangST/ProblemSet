//
// Created by bossw on 2022/10/20.
//

#include<iostream>
#include<vector>
#include<unordered_set>
#include<set>

using namespace std;

class Solution {
public:
    bool wordBreak(string s, vector<string> &wordDict) {
        unordered_set<string> dict;
        for (int i = 0; i < wordDict.size(); i++)
            dict.insert(wordDict[i]);
        set<int> success_idx;
        success_idx.insert(0);
        int max_success_idx = 0;
        for (int i = 1; i < s.length(); i++) {
            for (set<int>::iterator itor = success_idx.begin(); itor != success_idx.end(); itor++) {
                string sub = s.substr(*itor, i - *itor);
                if (dict.count(sub)) {
                    success_idx.insert(i);
                    break;
                }
            }
        }
        for (set<int>::iterator itor = success_idx.begin(); itor != success_idx.end(); itor++) {
            string sub = s.substr(*itor, s.length() + 1 - *itor);
            if (dict.count(sub)) {
                success_idx.insert(s.length());
                break;
            }
        }
        if (max_success_idx == s.length())
            return true;
        else
            return false;
    }
};

int main(void) {
    vector<string> wordDict{"apple", "pen"};
    string s = "applepenapple";
    cout << (new Solution)->wordBreak(s, wordDict) << endl;
    return 0;
}