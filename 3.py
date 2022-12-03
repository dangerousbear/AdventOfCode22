#%%
lines = open("Input/3.txt", "r").read().split("\n")
s = 0
for i in range(0,len(lines),3):
    (x,) = set(lines[i]).intersection(set(lines[i+1])).intersection(set(lines[i+2]))
    s += ord(x) - 96 if x.islower() else ord(x) - 38

print("Answer", s)
# %%
