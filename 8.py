#%%
import numpy as np

lines = open("Input/8.txt", "r").readlines()
Nr, Nc = len(lines), len(lines[0])-1
f = np.zeros((Nr, Nc), dtype=int)
for i, line in enumerate(lines):
    for j, c in enumerate(line.strip("\n")):
        f[i, j] = int(c)

# View length is 1 + index of first element not lower than the treehouse height (h)
vl = lambda arr,h : next((i+1 for i, x in enumerate(arr) if x >= h), len(arr))

# Product of N, W, S, E view lengths for height h
sight_prod = lambda r,c,h : vl(f[:r, c][::-1],h) * vl((f[r, :c])[::-1],h) * vl(f[r, c+1:],h) * vl(f[r+1:, c],h)

print("Answer", max( sight_prod(r,c, f[r,c]) for r in range(1, Nr-1) for c in range(1, Nc-1)))