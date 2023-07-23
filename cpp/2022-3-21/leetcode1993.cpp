#include <iostream>
#include <map>
#include <queue>
#include <vector>
using namespace std;
class LockingTree {
public:
    vector<int> parent;
    vector<int> lockers;
    multimap<int, int> tree;
    LockingTree(vector<int> &parent) {
        int n = parent.size();
        for (int i = 0; i < n; ++i) {
            this->parent.push_back(parent[i]);
            tree.insert(pair<int, int>(parent[i], i));
        }

        lockers.resize(parent.size(), -1);
    }

    bool lock(int num, int user) {
        if (-1 == lockers[num]) {
            lockers[num] = user;
            return true;
        }
        return false;
    }

    bool unlock(int num, int user) {
        if (lockers[num] == user) {
            lockers[num] = -1;
            return true;
        }
        return false;
    }

    bool upgrade(int num, int user) {
        if (-1 != lockers[num]) return false;
        //* find if the node has a locked parent
        int father = parent[num];
        while (-1 != father) {
            if (-1 != lockers[father]) return false;
            father = parent[father];
        }
        //* find if the node's children have been locked
        bool has_child_locked = false;
        queue<int> q;
        q.push(num);
        while (!q.empty()) {
            int current = q.front();
            q.pop();
            for (multimap<int, int>::iterator itor = tree.find(current);
                 itor != tree.end() && itor->first == current; itor++) {
                if (lockers[itor->second] != -1) {
                    has_child_locked = true;
                    lockers[itor->second] = -1;
                }
                q.push(itor->second);
            }
        }
        if (has_child_locked) {
            lockers[num] = user;
            return true;
        } else
            return false;
    }
};

/**
 * Your LockingTree object will be instantiated and called as such:
 * LockingTree* obj = new LockingTree(parent);
 * bool param_1 = obj->lock(num,user);
 * bool param_2 = obj->unlock(num,user);
 * bool param_3 = obj->upgrade(num,user);
 */
int main(void) {
    /*
    ["LockingTree","lock","unlock","unlock","lock","upgrade","lock"]
    [[[-1,0,0,1,1,2,2]],[2,2],[2,3],[2,2],[4,5],[0,1],[0,1]]
    */

    string op1[] = {"lock", "unlock", "unlock", "lock", "upgrade", "lock"};
    vector<string> op;
    int parent[] = {-1, 0, 0, 1, 1, 2, 2};
    vector<int> parent2;
    for (int i = 0; i < 7; i++) parent2.push_back(parent[i]);
    for (int i = 0; i < 6; i++) op.push_back(op1[i]);
    int op_detail[][2] = {{2, 2}, {2, 3}, {2, 2}, {4, 5}, {0, 1}, {0, 1}};

    LockingTree t(parent2);
    for (int i = 0; i < op.size(); i++) {
        if (op[i] == "lock")
            cout << t.lock(op_detail[i][0], op_detail[i][1]) << endl;
        else if (op[i] == "unlock")
            cout << t.unlock(op_detail[i][0], op_detail[i][1]) << endl;
        else
            cout << t.upgrade(op_detail[i][0], op_detail[i][1]) << endl;
    }
    cout << "ok" << endl;
    return 0;
}
