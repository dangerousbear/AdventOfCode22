#%%
lines = open("Input/21.txt", "r").readlines()


inp = []
for i, l in enumerate(lines):
    l = l.strip("\n").replace(":", " =").replace("/", "//")
    if "root" in l:
        l = l.replace("+","-")
    inp.append(l)
inp.sort(key=len)
# Horribly ugly solution. But it works...
goods = []
while True:
    bads = []
    for v in inp:
        try:
            exec(v)
            goods.append(v)
        except:
            bads.append(v)
    inp = bads
    if len(bads) == 0:
        break

N = 3305669217800 # Found by manual bisection search
for k1 in range(N, N+50):
    vsC = goods.copy()
    for i in range(len(vsC)):
        if vsC[i][:4] == "humn":
            vsC[i] = vsC[i][:7] + str(k1)
            break
    for v in vsC:
        exec(v)
    if (root == 0):
        print("Success!")
        break

print("Answer", k1)
# %%
