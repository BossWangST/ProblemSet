#include <iostream>
using namespace std;

const int N = 200005; // 我求求你看清楚题目里有几个 0 好吗？
int a[N], c[N];
int main(void)
{
    int t;
    cin >> t;

    while (t-- > 0)
    {
        int n;
        cin >> n;
        for (int i = 0; i < n; i++)
            cin >> a[i];
        int m = INT_MIN;
        int b;
        for (int i = 0; i < n; i++)
        {
            cin >> b;
            c[i] = a[i] - b;
            m = max(m, c[i]);
        }
        int res = 0;
        for (int i = 0; i < n; i++)
            res += c[i] == m ? 1 : 0;
        cout << res << endl;
        for (int i = 0; i < n; i++)
            if (c[i] == m)
                cout << i + 1 << " ";
        cout << endl;
    }
    return 0;
}