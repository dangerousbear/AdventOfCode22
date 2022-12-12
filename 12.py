#%%
import numpy as np
lines = open("Input/12t.txt", "r").readlines()
n_rows, n_cols = len(lines), len(lines[0])-1
H = np.zeros((n_rows, n_cols), dtype=int)
D = np.full((n_rows, n_cols), 10000, dtype=int)

for i, l in enumerate(lines):
    for j, c in enumerate(l):
        if (c.islower()):
            H[i,j] = ord(c) 
        elif c == "S":
            H[i,j] = ord('a')
        elif c == "E":
            H[i,j] = ord('z') 
            Er, Ec = i,j

def search(i,j, p_len): # Recursively searches downward
    if (p_len >= D[i,j]):
        return
    D[i,j] = p_len
    h = H[i,j]
    if i > 0 and H[i-1, j] >= h - 1:
        search(i-1, j, p_len+1)
    if j > 0 and H[i, j-1] >= h - 1:
        search(i, j-1, p_len+1)
    if i + 1 < n_rows and H[i+1, j] >= h - 1:
        search(i+1, j, p_len+1)
    if j + 1 < n_cols and H[i, j+1] >= h - 1:
        search(i, j+1, p_len+1)

    
search(Er, Ec, 0)

print(min(D[i,j] for j in range(n_cols) for i in range(n_rows) if H[i,j] == ord('a')))
