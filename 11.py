#%%
import functools as ft

lines = open("Input/11.txt", "r").readlines()

items, ops, test_vals, ok_targets, fail_targets = [],[],[],[],[]

def get_lambda(v, is_add):
    return (lambda x : x + v) if is_add else (lambda x : x * v)

for l in lines:
    toks = l.split(":")
    if "items" in toks[0]:
        items.append([int(x) for x in toks[1].split(",")])
    elif "eration" in toks[0]:
        if "old * old" in l:
            ops.append(lambda x : x * x)
        else:
            is_add = "+" in l
            ops.append(get_lambda(int(l[l.find("+" if is_add else "*")+1:]),is_add))
    elif "est" in toks[0]:
        test_vals.append(int(l[l.find("by")+3:]))
    elif "true" in toks[0]:
        ok_targets.append(int(l[l.find("ey")+3:]))
    elif "false" in toks[0]:
        fail_targets.append(int(l[l.find("ey")+3:]))

N = len(items)
counts = [0] * N

prod = 1
for v in test_vals:
    prod *= v

for r in range(10000):
    for k in range(N):
        for v  in items[k]:
            counts[k] += 1
            v = ops[k](v) % prod
            items[ok_targets[k] if v % test_vals[k] == 0 else fail_targets[k]].append(v)
        items[k] = []

counts.sort()
print(counts[-1] * counts[-2])
