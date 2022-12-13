#%%
import functools as ft
lines = [l.strip("\n") for l in open("Input/13.txt", "r").readlines() if l != "\n"]

def cmp(a,b):
    if isinstance(a,int) and isinstance(b,int):
        return -1 if a < b else a > b
    elif isinstance(a,list) and isinstance(b,list):
        # Return first nonzero cmp if exists, else compare lengths.
        nonzero_cmp = filter(lambda x : x != 0, [cmp(av, bv) for av,bv in zip(a,b)])
        return next(nonzero_cmp, -1 if len(a) < len(b) else len(a) > len(b)) 
    else:
        return cmp([a], b) if isinstance(a,int) else cmp(a,[b])

# Could be O(n) by just counting smaller elements instead of sorting, but whatever. 
signal = sorted([eval(l) for l in lines] + [[[2]], [[6]]], key=ft.cmp_to_key(cmp))

print("Answer", (1+signal.index([[2]])) * (1+signal.index([[6]])))
