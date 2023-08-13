from typing import *
from collections import *
from bisect import *
from functools import *
from math import *
from itertools import *
from heapq import *
from random import *
import sys

LIMIT = 2 * 10 ** 5 + 1
sys.setrecursionlimit(LIMIT)
n, m = map(int, input().split())
g = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    g[u - 1].append(v - 1)
    g[v - 1].append(u - 1)

'''
考虑最少要删掉多少条边才没有环比较难，正难则反，考虑最多能保留多少条边
假设结果是 res，最多能保留 l 条边，res = m - l
那么如何思考最多能保留多少条边？
假设现在一共就有 n 个点没有边，我们最多能加几条边而不出现环？
这不正是“树”的定义吗，所以最多加 n - 1 条边可以没有环，即两两相连
假设我们现在的题目就是这样，但不一定一开始的图是全部连上的，所以要考虑【连通部分】
对于每一个连通部分 S，设其有 x 个节点，那么这个 S 最多可以有 x - 1 条边
下面就是公式推导：图所有的节点数量 n = sum(x for each x in S)
而我们能最多的边数是 l = sum(x - 1 for each x in S) = sum(x for each x in S) - #S = n - #S
res = m - l = m - n + #S
'''
vis = [False for _ in range(n)]


def dfs(node: int):
    vis[node] = True
    for x in g[node]:
        if not vis[x]:
            dfs(x)


s = 0
for i in range(n):
    if not vis[i]:
        s += 1
        dfs(i)

print(m - n + s)
