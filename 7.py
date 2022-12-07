#%%
lines = open("Input/7.txt", "r").readlines()

tree = dict()
path = ""
for line in lines:
    line = line.strip("\n")
    if (line[:4] == "$ cd"):
        d = line[5:]
        if (d == "/"):
            path = "/"
        elif d == "..":
            path = path[:1+path[:-1].rfind("/")]
        else:
            path += d + "/"
    elif line[0] != "$":
        (v, name) = line.split()
        tree[path+name] =  int(v) if v != "dir" else -1


def size_all_sub_files(d): # Sum all files whose search path starts with d. Ugly, but works
    return sum(s for fp, s in tree.items() if d in fp and s > 0)

needed = 30000000 - (70000000 - size_all_sub_files("/"))
ans = 1e10
for fp, s in filter(lambda t : t[1] < 0, tree.items()):
    s = size_all_sub_files(fp)
    if (s >= needed and s < ans):
        ans = s

print("Answer", ans)

