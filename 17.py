#%%
import numpy as np

pushes = [c for c in open("Input/17.txt", "r").read()]

patterns = [[(0,0), (0,1), (0,2), (0,3)], [(0,1), (1,0), (1,1), (1,2), (2,1)], [(0,2), (1,2), (2,0), (2,1), (2,2)], [(0,0), (1,0), (2,0), (3,0)], [(0,0), (0,1), (1,0), (1,1)]]
row_offset = [0, -2, -2, -3, -1]

n_rows, n_cols = 100000, 7
f = np.zeros((n_rows, n_cols), dtype=int)

lowest_row = n_rows

def collision(r, c, p):
    for rd, cd in p:
        r2, c2 = r + rd, c + cd
        if r2 < 0 or c2 < 0 or c2 >= n_cols or r2 >= n_rows or f[r2, c2] != 0:
            # print("Collision at",r,c)
            return True
    return False

def draw_shape(r,c,p):
    for rd, cd in p:
        assert(f[r + rd, c + cd] == 0)
        f[r + rd, c + cd] = 5

push_idx = 0
for i in range(4500):
    shape_idx = i % 5
    p = patterns[shape_idx]
    r,c = lowest_row-4+row_offset[shape_idx], 2
    assert(r > 0)
    while True:
        push = 1 if pushes[push_idx] == ">" else -1
        push_idx = (push_idx + 1) % len(pushes)
        c += push
        if (collision(r,c,p)):
            c -= push
        r += 1
        if (collision(r,c,p)):
            r -= 1
            break
    draw_shape(r,c,p)
    lowest_row = min(lowest_row,r)

for rtest in range(n_rows):
    if 5 in f[rtest,:]:
        break

s = n_rows - rtest

print("Answer", s + 573065900 * 2767) # Numbers from math done outside