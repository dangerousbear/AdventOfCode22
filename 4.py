#%%
lines = open("Input/4.txt", "r").readlines()
s = 0
for line in lines:
    (l1, r1, l2, r2) = [int(x) for x in line.replace("-", ",").split(",")]
    s+= l1 <= r2 and r1 >= l2 or l2 <= r1 and r2 >= l1
print("Answer", s)
