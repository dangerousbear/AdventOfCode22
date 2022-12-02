#%%
lines = open("Input/2.txt", "r").read().split("\n")
letter_to_num = {"A" : 0, "B" : 1, "C" : 2, "X" : 0, "Y" : 1, "Z" : 2}
s = 0
for line in lines:
    toks = line.split()
    (p1, p2) = (letter_to_num[toks[0]], letter_to_num[toks[1]])
    p2 = (p1 + p2 - 1) % 3 #Part 2
    d = p2 - p1
    if (d == 1 or d == -2): 
        s += 6 
    elif (d == 0):
        s += 3
    s += p2 + 1
print("Answer", s)
# %%
