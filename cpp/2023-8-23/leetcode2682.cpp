#include <iostream>
using namespace std;

class Solution
{
public:
    vector<int> circularGameLosers(int n, int k)
    {
        bool vis[n];
        fill_n(vis, n, false);
        int p = 0;
        int turn = 1;
        while (true)
        {
            if (!vis[p])
                vis[p] = true;
            else
                break;
            p = (p + turn++ * k) % n;
        }
        vector<int> res;
        for (int i = 0; i < n; i++)
            if (!vis[i])
                res.push_back(i + 1);
        return res;
    }
};