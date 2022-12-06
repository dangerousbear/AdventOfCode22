#%%
line = open("Input/6.txt", "r").read()
N = 14
print(1+next(i for i in range(N, len(line)) if len(set(line[i:i-N:-1])) == N))

