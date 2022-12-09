#%%
import numpy as np

lines = open("Input/8.txt", "r").readlines()
n_rows, n_cols = len(lines), len(lines[0])-1
f = np.zeros((n_rows, n_cols), dtype=int)
for r in range(n_rows):
    for c in range(n_cols):
        f[r,c] = int(lines[r][c])

# Viewing distance of trees in arr is 1 + index of first element not lower than the treehouse height (h)
vd = lambda arr,h : next((i+1 for i, x in enumerate(arr) if x >= h), len(arr))

# Product of N, W, S, E view distances for height h. N & W are reversed using [::-1]
score = lambda r,c,h : vd(f[:r, c][::-1],h) * vd((f[r, :c])[::-1],h) * vd(f[r, c+1:],h) * vd(f[r+1:, c],h)

print(max(score(r,c, f[r,c]) for r in range(n_rows) for c in range(n_cols)))