#%%
import matplotlib as plt
import math
import numpy as np
import functools as ft
from collections import defaultdict
from itertools import chain, combinations

lines = open("Input/16.txt", "r").readlines()

# n_rows, n_cols = len(lines), len(lines[0])
# f = np.zeros((n_rows, n_cols), dtype=int)

G = dict()
flows = dict()

for i, l in enumerate(lines):
    l = l.strip("\n").replace("Valve ", "").replace(" has flow rate=", ",").replace(" tunnels lead to valves ", "").replace(" tunnel leads to valve ", "")
    # print(l)
    ts = l.split(";")
    v = int(ts[0][3:])

    tars = ts[1].split(", ")
    if (v > 0):
        flows[ts[0][:2]] = v
    G[ts[0][:2]] = tars

# print(G)    


nzD = dict()
for n in flows.keys():
    nzD[n] = defaultdict(lambda:10000)
nzD["AA"] = defaultdict(lambda:10000)
def search(n, P, d):
    # print("Time", time)
    d += 1
    if (P[n] < d):
        return
    P[n] = d
    for t in G[n]:
        search(t, P, d)

search("AA", nzD["AA"], 0)
for n in flows.keys():
    search(n, nzD[n], 0)

P = defaultdict(int)


def search(n, time, opened, path, totalFlowSoFar):
    assert(time >= 0)
    if n != "AA":
        path += n + " "
        opened.add(n)
    fSum = sum(flows[c] for c in opened)
    P[path] = totalFlowSoFar + time * fSum
    for t in flows.keys():
        if t not in opened:
            tDiff = nzD[n][t]
            if tDiff < time:
                search(t, time-tDiff, opened.copy(), path, totalFlowSoFar + tDiff * fSum)

search("AA", 26, set(), "", 0)

subsets = [[]]
for el in flows.keys():
    subsets += [s+[el] for s in subsets]

allK = set(flows.keys())
s = 0
for i, subset in enumerate(subsets):
    if i % 100 == 0:
        print(i)
    subset = set(subset)
    negation = allK.difference(subset)
    
    maxS, maxN = 0,0
    for path, v in P.items():
        path = path.split()
        if (all(k in subset for k in path)):
            maxS = max(maxS, v)
        if (all(k in negation for k in path)):
            maxN = max(maxN, v)
    s = max(s, maxS + maxN)



print("Answer", s)

# %%
