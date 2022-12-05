#%%
lines = open("Input/5.txt", "r").readlines()

split_idx = next(i for i,line in enumerate(lines) if "1" in line)
stacks = [[] for _ in range(len(lines[0])//4)]

for line in reversed(lines[:split_idx]):
    for i, c in enumerate(line[1::4]):
        if c != " ":
            stacks[i].append(c)

instructions = [(int(n), int(s)-1, int(t)-1) for n,s,t in [line.replace("move ", "").replace(" from ", " ").replace(" to ", " ").split() for line in lines[split_idx+2:]]]

for (n, s, t) in instructions:
    # Move the top n items from stack s to stack t
    stacks[t].extend(stacks[s][-n:])
    stacks[s] = stacks[s][:-n]

print("Answer", "".join([st[-1] for st in stacks]))