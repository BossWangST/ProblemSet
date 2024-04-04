#include <iostream>
#include <set>
#include <queue>
using namespace std;

class Solution
{
public:
    int smallestChair(vector<vector<int>> &times, int targetFriend)
    {
        vector<pair<int, int>> arrival;
        vector<pair<int, int>> leaving;
        int i = 0;
        for (auto &cur : times)
        {
            arrival.emplace_back(cur[0], i);
            leaving.emplace_back(cur[1], i++);
        }
        sort(arrival.begin(), arrival.end());
        sort(leaving.begin(), leaving.end());
        set<int> chair;
        int n = times.size();
        for (int i = 0; i < n; i++)
            chair.insert(i);
        unordered_map<int, int> index;
        int j = 0;
        for (auto &&[time, person] : arrival)
        {
            // 先释放被占用的椅子
            while (j < n && leaving[j].first <= time)
            {
                chair.insert(index[leaving[j++].second]);
            }
            int seat = *chair.begin();
            if (person == targetFriend)
                return seat;
            index[person] = seat;
            chair.erase(seat);
        }
        return -1;
    }
};