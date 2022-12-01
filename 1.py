lines = open("Input/1.txt", "r").readlines()

current_val = 0
vals = []
for line in lines:
    line = line.strip("\n")
    if (line == ""):
        vals.append(current_val)
        current_val = 0
    else:
        current_val += int(line)
    
vals.sort() # O(n log n), but fast to type!
print("Answer part 1", vals[-1])
print("Answer part 1", vals[-1] + vals[-2] + vals[-3])