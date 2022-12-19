#%%
from itertools import product

neighbors = lambda x,y,z : [(x+1,y,z), (x-1,y,z), (x,y+1,z), (x,y-1,z), (x,y,z+1), (x,y,z-1)]

inp = set([tuple([int(x) for x in l.split(",")]) for l in open("Input/18.txt", "r").readlines()])

max_x, max_y, max_z = max(c[0] for c in inp), max(c[1] for c in inp), max(c[2] for c in inp)
def find_trapped(c, searched):
    # print("Eval",c)
    if c in inp:
        return True
    if any(v < 0 for v in c) or c[0] == max_x or c[1] == max_y or c[2] == max_z:
        return False
    searched.add(c)
    return all(find_trapped(n, searched) for n in neighbors(*c) if n not in searched)

trapped = set()
for c in product(range(max_x), range(max_y), range(max_z)):
    if c not in inp and c not in trapped:
        cubes = set()
        if find_trapped(c,cubes):
            trapped.update(cubes)

surface = lambda cubes : sum(6 - sum(n in cubes for n in neighbors(*c)) for c in cubes)

s = surface(inp) - surface(trapped)

print("Answer", s)