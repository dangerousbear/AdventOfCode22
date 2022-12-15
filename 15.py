#%%
from collections import defaultdict
S = []
R = []
d = lambda p1, p2: abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

for l in open("Input/15.txt", "r").readlines():
    ts = l.strip("\n").replace("Sensor at ", "").replace(" closest beacon is at ", "").replace("x=", "").replace("y=", "").split(":")
    Sx, Sy = ts[0].split(",")
    Cx, Cy = ts[1].split(",")
    S.append((int(Sx), int(Sy)))
    R.append(d(S[-1], (int(Cx), int(Cy))))

# LIMIT = 20
L = 4000000

vs = defaultdict(int)

# Find points that lie exactly outside the (1-norm) circle for each scanner.
for i in range(len(S)):
    print("At", i)
    Sx, Sy = S[i]
    D = R[i] + 1
    for rd in range(max(-D, -Sy), min(D, L-Sy)+1):
        y = Sy + rd
        x1 = Sx + abs(D-rd)
        x2 = Sx - abs(D-rd)
        if x1 <= L:
            vs[(x1, y)] += 1
        if 0 <= x2:
            vs[(x2, y)] += 1

    
print("Num intersects", len(vs))

# Only consider points on two or more circles.
for p, _ in filter(lambda x : x[1] >= 2, vs.items()):
    if all(d(p,s) > r for s, r in zip(S,R)):
        # print("FOUND at ", p)
        print("Answer", 4000000 * p[0] + p[1])
        break