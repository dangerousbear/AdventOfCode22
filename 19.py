#%%
from collections import defaultdict

costs = [[int(x) for x in l.strip("\n").replace("Blueprint ", "").replace(": Each ore robot costs", "").replace("ore. Each clay robot costs ", "").replace("ore. Each obsidian robot costs ", "").replace(" ore and  ", "")\
    .replace(" clay. Each geode robot costs", "").replace(" ore and", "").replace(" obsidian.", "").split()] for l in open("Input/19.txt", "r").readlines()[:3]]

max_vals = defaultdict(int)

def search(ores, n_bots, t, C, buy_idx):
    if (buy_idx == 0):
        ores[0] -= C[1]
    elif (buy_idx == 1):
        ores[0] -= C[2]
    elif (buy_idx == 2):
        ores[0] -= C[3]
        ores[1] -= C[4]
    elif (buy_idx == 3):
        ores[0] -= C[5]
        ores[2] -= C[6]
    if (buy_idx != -1):
        n_bots[buy_idx] += 1
        ores[buy_idx] -= 1 # To compensate for extra ore generated from adding bot this round.

    if max_vals[C[0]] > ores[3] + (32 - t) * (5 + n_bots[3]):
        return # Heuristic to prune bad branches.
    
    could_build = [False] * 3
    while t < 32:
        t += 1
        t_rem = 32 - t
        should_build = lambda i, c : t_rem * n_bots[i] + ores[i] < t_rem * c and not could_build[i]
        for i, n in enumerate(n_bots):
            ores[i] += n
        if (ores[0] >= C[5] and ores[2] >= C[6]):
            search(ores.copy(), n_bots.copy(), t, C, 3)
            break # If we can build geo, always do it.
        if ores[0] >= C[1] and should_build(0, max(C[2], C[3], C[5])):
            could_build[0] = True
            search(ores.copy(), n_bots.copy(), t, C, 0)
        if (ores[0] >= C[2] and should_build(1, C[4])):
            could_build[1] = True
            search(ores.copy(), n_bots.copy(), t, C, 1)
        if (ores[0] >= C[3] and ores[1] >= C[4] and should_build(2, C[6])):
            could_build[2] = True
            search(ores.copy(), n_bots.copy(), t, C, 2)
            
    max_vals[C[0]] = max(max_vals[C[0]], ores[3])

     
for C in costs:
    t = 1
    n_bots = [1, 0, 0, 0]
    ores = [1,0,0,0]
    search(ores.copy(), n_bots.copy(), t, C, -1)

p = 1
for k, v in max_vals.items():
    p *= v

print("Answer", p)