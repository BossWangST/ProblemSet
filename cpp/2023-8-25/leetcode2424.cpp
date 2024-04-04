#include <iostream>
using namespace std;

class LUPrefix
{
public:
    int p;
    vector<bool> vis;
    LUPrefix(int n)
    {
        p = 0;
        for (int i = 0; i < n; i++)
            vis.push_back(false);
    }

    void upload(int video)
    {
        video--;
        vis[video] = true;
        while (p < vis.size() && vis[p]) p++;
    }

    int longest()
    {
        return p;
    }
};

/**
 * Your LUPrefix object will be instantiated and called as such:
 * LUPrefix* obj = new LUPrefix(n);
 * obj->upload(video);
 * int param_2 = obj->longest();
 */