//
// Created by bossw on 2022/10/20.
//

#include<iostream>
#include<vector>
#include<set>

using namespace std;

class Solution {
public:
    int global_target;
    int candidates_len;
    vector<int> global_candidates;
    vector<vector<int>> res;

    void dfs(int idx, vector<int> &current, int total) {
        if (total == global_target) {
            res.push_back(current);
            return;
        }
        if (idx >= candidates_len || total > global_target)
            return;

        // use candidate[i]
        current.push_back(global_candidates[idx]);
        dfs(idx, current, total + global_candidates[idx]);
        current.pop_back();
        // Forbid using candidate[i]
        dfs(idx + 1, current, total);
    }

    vector<vector<int>> combinationSum(vector<int> &candidates, int target) {
        global_target = target;
        candidates_len = candidates.size();
        global_candidates = candidates;
        vector<int> current(0);
        dfs(0, current, 0);
        return res;
    }
};

int main(void) {
    vector<int> candidates{2, 3, 6, 7};
    (new Solution)->combinationSum(candidates, 7);
    return 0;
}