#%%
import numpy as np

lines = open("Input/9.txt", "r").readlines()
dir2vec = {"U" : [0,1], "R" : [1,0], "D": [0, -1], "L" : [-1, 0]}
x = [np.array([0,0]) for _ in range(10)] # The rope, head is x[0]
visited = set()
for line in lines:
    dir, v = line.strip("\n").split()
    for _ in range(int(v)):
        x[0] += np.array(dir2vec[dir])
        for next, this in zip(x,x[1:]):
            d = next-this
            if (abs(d).max() > 1):
                this += np.clip(d,-1,1) # Never move more than 1 step in each dir
        visited.add(x[-1].tostring())

print(len(visited))