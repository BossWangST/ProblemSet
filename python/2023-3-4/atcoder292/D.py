from functools import *
from typing import *
from itertools import *
from math import *
from collections import *

N, M = list(map(int, input().split()))
g = defaultdict(set)
while M > 0:
    M -= 1
    u, v = list(map(int, input().split()))
    g[u].add(v)
    g[v].add(u)


def dfs(node: int, visited: List[bool], father: int) -> None:
    global cur_v, cur_e, cycle
    cur_v += 1
    visited[node] = True
    for cur in g[node]:
        if cur == node:
            cur_v += 1
            cur_e += 1
            continue
        if visited[cur] and cur != father:
            cur_e += 1
            cycle = True
            continue
        if visited[cur]:
            continue
        else:
            cur_e += 1
            dfs(cur, visited, node)


v, e = 0, 0
visited = [False for _ in range(N + 1)]
flag = True
for i in range(1, N + 1):
    if not visited[i]:
        cycle = False
        cur_v, cur_e = 0, 0
        dfs(i, visited, 0)
        if cycle:
            cur_e -= 1
        if v == 0:
            v, e = cur_v, cur_e
        else:
            if cur_v != v or cur_e != e:
                flag = False
                print('No')
                break
if flag:
    print('Yes')
