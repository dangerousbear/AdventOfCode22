#%%
import numpy as np

lines = open("Input/9.txt", "r").readlines()
dir2vec = {"U" : [0,1], "R" : [1,0], "D": [0, -1], "L" : [-1, 0]}
moves = []
for line in lines:
    d, v = line.strip("\n").split()
    moves.extend([np.array(d) for _ in range(int(v))])

x = [np.array([0,0]) for _ in range(10)] # The rope, head is x[0]
visited = set()

for m in moves:
    x[0] += m
    for next, this in zip(x,x[1:]):
        d = next-this
        if (abs(d).max() > 1):
            this += np.clip(d,-1,1) # Never move more than 1 step in each dir
    visited.add(x[-1].tostring())

print(len(visited))