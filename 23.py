#%%
lines = open("Input/23.txt", "r").readlines()

def dir2nbors(i,j, dir): 
    if dir == "N":
        return {(i-1, j), (i-1,j-1), (i-1, j+1)}
    if dir == "S" : 
        return {(i+1, j), (i+1,j-1), (i+1, j+1)}
    if dir ==  "W": 
        return {(i, j-1), (i-1,j-1), (i+1, j-1)}
    if dir == "E": 
        return {(i, j+1), (i-1,j+1), (i+1, j+1)}

def dir2move(i,j, dir): 
    if dir == "N":
        return (i-1, j)
    if dir == "S" : 
        return (i+1, j)
    if dir ==  "W": 
        return (i, j-1)
    if dir == "E": 
        return (i, j+1)

elves = set([(i,j) for i, l in enumerate(lines) for j, c in enumerate(l) if c == "#"])
dirs = ["N", "S", "W", "E"]

for round in range(5000):
    moves = []
    for i,j in elves:
        good_pos = [dir2move(i,j,dir) for dir in dirs if dir2nbors(i,j,dir).isdisjoint(elves)]
        if len(good_pos) > 0 and len(good_pos) < 4:
            moves.append(((i,j),good_pos[0]))


    moves.sort(key=lambda x:x[1])
    moved = False
    for idx, (e, new_pos) in enumerate(moves):
        if (idx == 0 or new_pos != moves[idx-1][1]) and (idx + 1 == len(moves) or new_pos != moves[idx+1][1]):
            elves.remove(e)
            elves.add(new_pos)
            moved = True
    
    if not moved:
        print("Answer", round+1)
        break
    dirs.append(dirs.pop(0))
