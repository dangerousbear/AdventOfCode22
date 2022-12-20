#%%
inp = [int(l) * 811589153 for l in open("Input/20.txt", "r").readlines()]

V = list(enumerate(inp.copy()))
for _ in range(10):
    for i, v in enumerate(inp):
        pos = V.index((i,v))
        V.insert((pos+v) % (len(V) - 1), V.pop(pos))

i0 = V.index((inp.index(0), 0))
print("Answer", V[(i0+1000) % len(V)][1] + V[(i0+2000) % len(V)][1] + V[(i0+3000) % len(V)][1])