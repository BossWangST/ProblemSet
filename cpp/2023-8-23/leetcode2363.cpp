#include <iostream>
using namespace std;

class Solution
{
public:
    vector<vector<int>> mergeSimilarItems(vector<vector<int>> &items1, vector<vector<int>> &items2)
    {
        unordered_map<int, int> d;
        for (auto item : items1)
        {
            // d.insert({item[0], item[1]});
            d[item[0]] = item[1];
        }
        for (auto item : items2)
        {
            if (d.find(item[0]) != d.end())
            {
                d[item[0]] += item[1];
            }
            else
            {
                // d.insert({item[0], item[1]});
                d[item[0]] = item[1];
            }
        }
        vector<vector<int>> res;
        for (auto iter : d)
        {
            res.push_back(vector<int>{iter.first, iter.second});
        }
        sort(res.begin(), res.end(), [](const vector<int> &a, const vector<int> &b)
             { return a[0] < b[0]; });
        return res;
    }
};

int main(void)
{
    vector<vector<int>> items1{{1, 1}, {4, 5}, {3, 8}};
    vector<vector<int>> items2{{3, 1}, {1, 5}};
    auto res = (new Solution())->mergeSimilarItems(items1, items2);
    cout << res.size() << endl;
    return 0;
}