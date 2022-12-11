#%%
import numpy as np
import math


lines = open("Input/10.txt", "r").readlines()

n_rows, n_cols = 6, 42

f = np.zeros((n_rows, n_cols), dtype=int)

X = 1
c = 0

def draw(c):
    r_idx = c // 40
    c_idx = c - 40 * r_idx
    if abs(c_idx - X) <= 1:
        f[r_idx, c_idx] = 5
    
for l in lines:
    toks = l.split()
    if toks[0] == "noop":
        draw(c)
    else:
        draw(c)
        c+= 1
        draw(c)
        X += int(toks[1])
    c+=1

print(f)