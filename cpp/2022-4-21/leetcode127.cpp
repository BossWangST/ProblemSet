#include <iostream>
#include <queue>
#include <vector>
using namespace std;
class Solution {
public:
    int ladderLength(string beginWord, string endWord,
                     vector<string>& wordList) {
        queue<int> q;
        if (find(wordList.begin(), wordList.end(), beginWord) == wordList.end())
            wordList.push_back(beginWord);
        vector<bool> visited(wordList.size(), false);
        vector<int> step(wordList.size(), 0);
        string current = "";
        while (!q.empty()) {
            current = q.front();
            q.pop();
        }
    }
};
int main() { return 0; }

