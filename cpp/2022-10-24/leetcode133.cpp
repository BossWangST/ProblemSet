//
// Created by bossw on 2022/10/24.
//

#include<iostream>
#include<vector>
#include<queue>
#include<unordered_set>
#include<unordered_map>


using namespace std;

// Definition for a Node.
class Node {
public:
    int val;
    vector<Node *> neighbors;

    Node() {
        val = 0;
        neighbors = vector<Node *>();
    }

    Node(int _val) {
        val = _val;
        neighbors = vector<Node *>();
    }

    Node(int _val, vector<Node *> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};

class Solution {
public:
    vector<Node *> copy(vector<Node *> origin) {
        vector<Node *> *clone = new vector<Node *>(0);
        if (origin.size() == 0)
            return *clone;
        for (int i = 0; i < origin.size(); i++)
            clone->push_back(origin[i]);
        return *clone;
    }

    Node *cloneGraph(Node *node) {
        unordered_map<int, Node *> maps;
        if (node == NULL)
            return NULL;
        Node *clone = new Node(node->val, copy(node->neighbors));
        //clone->val = node->val;
        //clone->neighbors = copy(node->neighbors);
        queue<Node *> q_origin;
        queue<Node *> q_clone;
        q_origin.push(node);
        q_clone.push(clone);

        maps.insert({clone->val, clone});
        while (!q_origin.empty()) {
            Node *cur_origin = q_origin.front();
            q_origin.pop();
            Node *cur_clone = q_clone.front();
            q_clone.pop();
            for (int i = 0; i < cur_origin->neighbors.size(); i++) {
                if (maps.count(cur_origin->neighbors[i]->val)) {
                    cur_clone->neighbors[i] = maps[cur_origin->neighbors[i]->val];
                } else {
                    Node *cur_buddy = new Node(cur_origin->neighbors[i]->val,
                                               copy(cur_origin->neighbors[i]->neighbors));
                    //cur_buddy->val = cur_origin->neighbors[i]->val;
                    //cur_buddy->neighbors = copy(cur_origin->neighbors[i]->neighbors);
                    cur_clone->neighbors[i] = cur_buddy;
                    q_origin.push(cur_origin->neighbors[i]);
                    q_clone.push(cur_buddy);
                    maps.insert({cur_buddy->val, cur_buddy});
                }
            }
        }
        return clone;
    }
};

int main(void) {
    return 0;
}