#%%
lines = open("Input/5.txt", "r").readlines()

split_idx = next(i for i,line in enumerate(lines) if "1" in line) 
stacks = [[], [], [], [], [], [], [], [], []]
for line in reversed(lines[:split_idx]):
    for i, c in enumerate(line[1::4]):
        if c != " ":
            stacks[i].append(c) 
instructions = [[int(x) for x in line.replace("move ", "").replace(" from ", ",").replace(" to ", ",").split(",")] for line in lines[split_idx+2:]]

for (n, s, t) in instructions: 
    stacks[t-1].extend(stacks[s-1][-n:])
    stacks[s-1] = stacks[s-1][:-n]

print("Answer", "".join([st[-1] for st in stacks]))
