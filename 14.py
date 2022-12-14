#%%
import numpy as np
lines = open("Input/14.txt", "r").readlines()

walls = [[tuple(map(lambda x : int(x), ts.split(","))) for ts in l.split("->")] for l in lines]

x_max =  max(max(p[0] for p in w) for w in walls) + 150 # Extra offset
y_max =  max(max(p[1] for p in w) for w in walls)
f = np.zeros((y_max+3, x_max), dtype=int)

for w in walls: # Fill in walls
    for (x,y), (x2, y2) in zip(w,w[1:]):
        if (x == x2):
                for yv in range(min(y,y2), max(y,y2) + 1):
                    f[yv, x] = 5
        else:
            for xv in range(min(x,x2), max(x,x2) + 1):
                f[y, xv] = 5

for xv in range(x_max):
    f[y_max+2, xv] = 5

def fall(i,j):
    for j_next in {j, j-1, j+1}:
        if f[i+1, j_next] == 0:
            fall(i+1,j_next)
            return
    f[i,j] = 1

s_x = 500
while True:
    fall(0, s_x)
    if (f[0, s_x] == 1):
        print("Answer", np.count_nonzero(f == 1))
        break