#include <iostream>
#include <set>
using namespace std;

class NumberContainers
{
public:
    unordered_map<int, set<int>> d; // memo number indexes
    unordered_map<int, int> num;    // track each index with number
    NumberContainers()
    {
    }

    void change(int index, int number)
    {
        auto cur = num.find(index);
        if (cur == num.end())
        {
            num[index] = number;
            d[number].insert(index);
        }
        else
        {
            d[cur->second].erase(index);
            num[index] = number;
            d[number].insert(index);
        }
    }

    int find(int number)
    {
        auto res = d.find(number);
        if (res == d.end() || res->second.size() == 0)
            return -1;
        else
            return *d[number].begin();
    }
};

/**
 * Your NumberContainers object will be instantiated and called as such:
 * NumberContainers* obj = new NumberContainers();
 * obj->change(index,number);
 * int param_2 = obj->find(number);
 */