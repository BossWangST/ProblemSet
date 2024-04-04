#include <iostream>
using namespace std;

class Solution
{
public:
    int maxDistToClosest(vector<int> &seats)
    {
        int res = 0;
        int i = 0;
        for (; i < seats.size(); i++)
        {
            if (seats[i] == 1)
                break;
        }
        res = max(res, i++);
        int distance = 0;
        for (; i < seats.size(); i++)
        {
            if (seats[i] == 1)
            {
                if (distance & 1)
                    res = max(res, distance / 2 + 1);
                else
                    res = max(res, distance / 2);
                distance = 0;
            }
            else
                distance++;
        }
        return max(res, distance);
    }
};
