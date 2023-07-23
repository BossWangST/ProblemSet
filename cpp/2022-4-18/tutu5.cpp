#include <iostream>
#include <map>
#include <queue>
#include <vector>
#define INF 1e15
using namespace std;
using ll = long long;
typedef pair<ll, ll> iPair;
class graph {
public:
    ll V;
    ll E;
    map<string, ll> name_list;
    vector<vector<iPair>> adj;
    graph(ll n, ll m) {
        V = n;
        E = m;
        adj.resize(n);
        string s, v;
        ll t;
        ll index = 0;
        for (ll i = 0; i < m; i++) {
            ll current_s, current_t;
            cin >> s >> v >> t;
            map<string, ll>::iterator itor;
            itor = name_list.find(s);
            if (itor == name_list.end()) {
                name_list.insert({s, index});
                current_s = index++;
            } else
                current_s = itor->second;
            itor = name_list.find(v);
            if (itor == name_list.end()) {
                name_list.insert({v, index});
                current_t = index++;
            } else
                current_t = itor->second;
            adj[current_s].push_back({current_t, t});
            // adj[current_t].push_back({current_s, t});
        }
    }
    ll calculate(string s, string v) {
        map<string, ll>::iterator itor;
        itor = name_list.find(s);
        ll s_index, v_index;
        if (itor == name_list.end())
            return -1;
        else
            s_index = name_list.find(s)->second;
        itor = name_list.find(v);
        if (itor == name_list.end())
            return -1;
        else
            v_index = name_list.find(v)->second;
        priority_queue<iPair, vector<iPair>, greater<iPair>> pq;
        vector<ll> dis(V, INF);
        vector<bool> visited(V, false);
        pq.push({0, s_index});
        dis[s_index] = 0;
        while (!pq.empty()) {
            ll u = pq.top().second;
            pq.pop();
            if (u == v_index) return dis[v_index];
            if (visited[u]) continue;
            visited[u] = true;
            for (auto x : adj[u]) {
                ll index = x.first;  // u可以到index
                ll weight = x.second;
                if (dis[u] + weight < dis[index]) {
                    dis[index] = dis[u] + weight;
                    pq.push({dis[index], index});
                }  //我到index比我先到u再到index要多，则走u到index更短
            }
        }
        return -1;
    }
};
int main() {
    ll n, m;
    cin >> n >> m;
    graph g(n, m);

    ll q;
    cin >> q;
    string s, v;
    while (q--) {
        cin >> s >> v;
        ll current_res = g.calculate(s, v);
        if (-1 == current_res)
            cout << "INF" << endl;
        else
            cout << current_res << endl;
    }
    return 0;
}

