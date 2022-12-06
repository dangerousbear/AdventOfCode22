#%%
line = open("Input/6.txt", "r").read()
N = 14
print(next(i for i in range(N, len(line)) if len(set(line[i-N:i])) == N))

