#%%
lines = open("Input/7.txt", "r").readlines()

files = dict()
path = ""
for line in lines:
    line = line.strip("\n")
    if (line[:4] == "$ cd"):
        new = line[5:]
        if (new == "/"):
            path = "/"
        elif new == "..":
            path = path[:1+path[:-1].rfind("/")]
        else:
            path += new + "/"
    elif line[0] != "$":
        (v, name) = line.split()
        files[path+name] =  int(v) if v != "dir" else -1


def size_all_sub_files(d): #Ugly, but works
    return sum(s for fp, s in files.items() if d in fp and len(fp) > len(d) and s > 0)

needed = 30000000 - (70000000 - size_all_sub_files("/"))
ans = 1e10
for fp, s in files.items():
    if s < 0:
        s = size_all_sub_files(fp)
    if (s >= needed and s < ans):
        ans = s

print("Answer", ans)

